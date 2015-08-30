from tastypie.utils.timezone import now
from django.utils.text import slugify
from django.db import models

class SensorData(models.Model):
	# csa_1, csa_4 etc, the module that reported this
	sensor_name = models.CharField(max_length=10)
	# mens washroom, etc
	sensor_location = models.CharField(max_length=20)
	entry_date = models.DateTimeField(default=now)

	def save(self, *args, **kwargs):
		super(SensorData, self).save(*args, **kwargs)

	@classmethod
	def create(self, location="undefined", name=""):
		sensordata = self(sensor_location=location, sensor_name = name)

		return sensordata

#class TowelStatistics(models.Model):
# class Dispenser(models.Model):
	# name = models.CharField(max_length=10, unique=True)
    # def __init__(self):
        # # alive or dead 
        # self.lastKnownSensorState = "unknown"
        # self.lcdState = "disabled"
        # self.paperTowelState = "full"
        # self.pulls = 0
        # self.lastPull
