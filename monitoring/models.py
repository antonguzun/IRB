from django.db import models


class Perimeter(models.Model):
    name = models.CharField(max_length=100, null=False)


class Device(models.Model):
    perimeter = models.ForeignKey(Perimeter, related_name="devices", on_delete=models.CASCADE)
    address = models.IntegerField(null=False)
    configuration = models.IntegerField(null=False, default=72)


class DevicesState(models.Model):
    device = models.ForeignKey(Device, related_name="states", on_delete=models.CASCADE)
    state_of_rays = models.CharField(max_length=72, default=(72*'^'))
    power = models.FloatField(null=False)
    pub_date = models.DateField(null=False)