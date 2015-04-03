from random import randint
from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.resources import ModelResource, Resource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from dashboard.models import SensorData

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
    usage_average = fields.IntegerField(attribute='usage_average')
    usage_most_perc = fields.IntegerField(attribute='usage_most_perc')
    usage_least_perc = fields.IntegerField(attribute='usage_least_perc')
    cost_current = fields.FloatField(attribute='cost_current')
    cost_projected_daily = fields.IntegerField(attribute='cost_projected_daily')
    value = fields.IntegerField(attribute='value')
    random = fields.IntegerField(attribute='random')

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
        setattr(setting, 'value', f)
        setattr(setting, 'random', randint(1, 1000))
        setattr(setting, 'cost_current', len(SensorData.objects.all()) * 0.01)
        setattr(setting, 'cost_projected_daily', randint(3600, 3750) + f)
        return setting
