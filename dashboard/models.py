from tastypie.utils.timezone import now
from django.utils.text import slugify
from django.db import models

class SensorData(models.Model):
	sensor_location = models.CharField(max_length=20)
	entry_date = models.DateTimeField(default=now)

	def save(self, *args, **kwargs):
		super(SensorData, self).save(*args, **kwargs)
