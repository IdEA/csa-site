from random import randint
from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.resources import ModelResource, Resource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from dashboard.models import SensorData

import paho.mqtt.client as mqtt
import threading


class mqttThread(threading.Thread):
    def __init__(self, threadID, client):
        threading.Thread.__init__(self)
        self.threadID = threadID

        self.client = client
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set("CSA_TEST", "CSA_TEST")
        self.client.connect("stevenhuang.ca", 12001, 60)
        self.client.publish("/test", "csa-site client mqtt connected")
        self.pulls = 0
        self.dispenser = {}


    def run(self):
        print("MQTT Thread starting...")
        self.client.loop_start()
        """
        while True:
            prin("ay")
            self.client.loop()
        """

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        #self.client.subscribe("$SYS/#")
        self.client.subscribe("dispenser/#")
        self.client.subscribe("connCheck/#")
        self.client.subscribe("action/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        topics = msg.topic.split("/")
        try:
            # msg from a module
            if topics[0] == "dispenser":
                if len(topics) == 2:
                    if msg.payload == "pull":
                        print("Detected pull from %s" % topics[1])
                        newEntry = SensorData.create(name=topics[1])
                        newEntry.save()
                        self.pulls += 1
                    elif msg.payload == "alive":
                        print("Alive: %s" % topics[1])
                        #getattr(self.dispenser.
                    elif msg.payload == "dead":
                        print("Dead: %s" % topics[1])
                elif len(topics) == 3:
                    if topics[2] == "status":
                        print("Recieved status update from" % topics[1])
            # TODO: authorize this
            elif topics[0] == "action":
                if topics[1] == "delete":
                    if topics[2] == "entries" and msg.payload == "yesrly":
                        print("Deleting all entries")
                        SensorData.objects.all().delete()
        except IndexError:
            print("Index error... ignoring")


        print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
mqttClientThread = mqttThread(1, client)
mqttClientThread.start();

class SensorDataResource(ModelResource):
	class Meta:
		queryset = SensorData.objects.all()
                authorization = Authorization()
                #authentication = BasicAuthentication()
		resource_name = 'entry'

class StatisticsObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}
        setattr(self, 'usage_average', 3)
        setattr(self, 'usage_most_perc', 64)
        setattr(self, 'usage_least_perc', 23)
        setattr(self, 'sample_latitude', 49.27688300)
        setattr(self, 'sample_longitude', -122.914845000000010)

        if initial:
            self.update(initial)

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def update(self, other):
        for k in other:
            self.__setattr__(k, other[k])

    def to_dict(self):
        return self._data

f = 0
setting = StatisticsObject()
class StatisticsResource(Resource):
    # static
    usage_average = fields.IntegerField(attribute='usage_average')
    usage_most_perc = fields.IntegerField(attribute='usage_most_perc')
    usage_least_perc = fields.IntegerField(attribute='usage_least_perc')
    sample_latitude = fields.FloatField(attribute='sample_latitude')
    sample_longitude = fields.FloatField(attribute='sample_longitude')
    # dynamic
    test_value = fields.IntegerField(attribute='test_value')
    random = fields.IntegerField(attribute='random')
    cost_current = fields.FloatField(attribute='cost_current')
    cost_projected_daily = fields.IntegerField(attribute='cost_projected_daily')

    class Meta:
        resource_name = 'statistics'
        object_class = StatisticsObject
        authorization = Authorization()

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}
        return kwargs

    def get_object_list(self, request):
        return [self.obj_get()]

    def obj_get_list(self, request=None, **kwargs):
        return [self.obj_get()]

    def obj_get(self, request=None, key=None, **kwargs):
        global f, setting
        f += 1
        setattr(setting, 'test_value', f)
        setattr(setting, 'random', randint(1, 1000))
        setattr(setting, 'cost_current', SensorData.objects.count() * 0.01)
        setattr(setting, 'cost_projected_daily', randint(3600, 3750) + f)
        return setting

        # indented to comment out
        def alter_detail_data_to_serialize(self, request, data):
                print("hit")
                if request.GET.get('meta_only'):
                        return {'meta': data['meta']}
                elif request.GET.get('count_only'):
                        return {'total_count': data['meta']['total_count']}
                return {}

        def alter_list_data_to_serialize(self, request, data):
                print("hit")
                if request.GET.get('meta_only'):
                        return {'meta': data['meta']}
                elif request.GET.get('count_only'):
                        return {'total_count': data['meta']['total_count']}
                return {}
