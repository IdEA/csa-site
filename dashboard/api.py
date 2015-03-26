from tastypie.resources import ModelResource
from dashboard.models import SensorData

class SensorDataResource(ModelResource):
	class Meta:
		queryset = SensorData.objects.all()
		resource_name = 'entry'

