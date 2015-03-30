from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from dashboard.models import SensorData

class SensorDataResource(ModelResource):
	class Meta:
		queryset = SensorData.objects.all()
                authentication = BasicAuthentication()
		resource_name = 'entry'

