from django.db import models

class GPS(models.Model):
    _id = models.CharField(max_length = 20)
    latitude = models.DecimalField(max_digits=25, decimal_places=20, blank = True, null = True)
    longitude = models.DecimalField(max_digits=25, decimal_places=20, blank = True, null =True)
    altitude = models.DecimalField(max_digits=10, decimal_places=5, blank = True, null = True)
    temperature = models.DecimalField(max_digits=10, decimal_places=5, blank = True, null = True)
    datetime = models.DateTimeField(auto_now=True)

class Fleet(models.Model):
    fleet_id = models.CharField(max_length = 20)
    ids = models.CharField(max_length = 300)

class Obstructions(models.Model):
    by = models.ForeignKey(GPS, on_delete= models.CASCADE)
    latitude = models.DecimalField(max_digits=25, decimal_places=20, blank = True, null = True)
    longitude = models.DecimalField(max_digits=25, decimal_places=20, blank = True, null =True)
    altitude = models.DecimalField(max_digits=10, decimal_places=5, blank = True, null = True)
    distance = models.FloatField( blank = True, null = True)