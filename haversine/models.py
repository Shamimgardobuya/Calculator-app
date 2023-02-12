from django.db import models
# Create your models here.
from enum import Enum
import haversine
from math import radians,asin,sqrt,cos,sin

class Unitts(Enum):
       KM= "Kilometre"
       M = "Metre"
class Speed(models.Model):
   
    measurementunit=models.CharField(max_length=18,choices=[(tag,tag.value) for tag in Unitts]),
    speed=models.IntegerField()
        
class Position(models.Model):
    latitude=models.DecimalField(max_digits=19,decimal_places=8)
    longitude=models.DecimalField(max_digits=26,decimal_places=8)
    latitude_two=models.DecimalField(max_digits=19,decimal_places=8,null=True)
    longitude_two=models.DecimalField(max_digits=26,decimal_places=8,null=True)
    speed_of_car=models.DecimalField(max_digits=26,decimal_places=8,null=True)

    
    @property
    def calculating(self):
        lat= self.latitude
        l=radians(lat)
        long=self.longitude
        l2=radians(long) 
        lat_two=self.latitude_two
        p=radians(lat_two)
        long_two=self.longitude_two
        p2=radians(long_two)
        difference_lat=l-p
        difference_long=l2-p2
        formula=sin(difference_lat/2)**2 + cos(l)*cos(p)*sin(difference_long/2)**2
        inverse=2*asin(sqrt(formula))
        earth_radius=6371
        distance=inverse*earth_radius
        return 'hello'
    

class Place(models.Model):
    place_one=models.CharField(max_length=90,null=True)
    location=models.ForeignKey(related_name='location',to=Position,on_delete=models.CASCADE)
    place_two=models.CharField(max_length=90,null=True)
    location_two=models.ForeignKey(related_name='location_two',to=Position,on_delete=models.CASCADE,null=True)

     
    def __str__(self):
         return f'{self.place_one} {self.place_two}'
    def calculatings(self,location,location_two):
        lat= location[0]
        l=radians(lat)
        l=radians(lat)
        long=self.longitude
        l2=radians(long) 
        lat_two=self.latitude_two
        p=radians(lat_two)
        long_two=self.longitude_two
        p2=radians(long_two)
        difference_lat=l-p
        difference_long=l2-p2
        formula=sin(difference_lat/2)**2 + cos(l)*cos(p)*sin(difference_long/2)**2
        inverse=2*asin(sqrt(formula))
        earth_radius=6371
        distance=inverse*earth_radius
        long=location[1]
        l2=radians(long) 
        lat_two=location_two[0]
        p=radians(lat_two)
        long_two=location_two[1]
        p2=radians(long_two)
        difference_lat=l-p
        difference_long=l2-p2
        formula=sin(difference_lat/2)**2 + cos(l)*cos(p)*sin(difference_long/2)**2
        inverse=2*asin(sqrt(formula))
        earth_radius=6371
        distance=inverse*earth_radius
        
        return distance



