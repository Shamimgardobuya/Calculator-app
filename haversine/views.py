from django.shortcuts import render,redirect
# from django.contrib import messages
from django import forms
from django.urls import reverse
from .models import Place, Position
# Create your views here.
from .forms import PositionForm
import haversine
# from . haversinee import haversine

# from .models import Place.calculating
from django.http import HttpResponse


#create a function and pass in request as a parameter
#check if request.method is post
#create an instance of the form that will capture the data
#check if form  is valid 
#if valid then save the data
#create else condition to handle if request is not post
#create a variable to handle the data 
#return the template
from math import radians,asin,sqrt,cos,sin

def create_position(request):

    if request.method == 'POST':

        form=PositionForm(request.POST)
        latitude=request.POST.get("latitude")
        longitude=request.POST.get("longitude",False)
        latitude_two=request.POST.get("latitude_two",False)
        longitude_two=request.POST.get("longitude_two",False)
        l=radians(int(float(latitude)))
        l2=radians(int(float(longitude)))
        p=radians(int(float(latitude_two)))
        p2=radians(int(float(longitude_two)))
        difference_lat=l-p
        difference_long=l2-p2
        formula=sin(difference_lat/2)**2 + cos(l)*cos(p)*sin(difference_long/2)**2
        inverse=2*asin(sqrt(formula))
        earth_radius=6371
        distance=inverse*earth_radius
        print(distance)
        return HttpResponse(distance)

            
    else:
        form=PositionForm()
        
    return render(request,'haversine/haversineform.html',{'hform':form})

def havepage(request):
        
        return render (request, 'haversine/resultt.html',{'ans':'latitude'})

    


def calculate_position(request):

    # # places=Place.objects.filter(places__contains=-1.89083940)
    # lyon = (45.7597, 4.8422) # (lat, lon)
    # paris = (48.8567, 2.3508)
    # ans=haversine(lyon, paris)
    z=haversine(53.32055555555556,-1.7297222222222221,53.31861111111111, -1.6997222222222223)
    
    return render (request, 'haversine/resultt.html',{'ans':z})


#create a function that calculates the shortest distance between two spherical points using the Haversine method

#import math 
#create a variable for holdnig two points both lat and long
#using the radians function convert positions to degrees
#find differece between the latitude and longitudes
#multiply each with their cosines and sines
#use the earth's radius to get distance in kilometeres








# def haversinee(request):
                
#                 form=PositionForm(request.POST)
            
#                 ans='hello'
            
#                 return render(request,'haversine/resultt.html',{'ans':ans})

# def calculating_haversine(request):
#     if request.method == 'post':
        

    # cleaned_data = super(PositionForm, self).clean()
    # latitude = cleaned_data.get('latitude')
    # longitude = cleaned_data.get('longitude')
    # latitude_two = cleaned_data.get('latitude_two')
    # longitude_two = cleaned_data.get('longitude_two')
    # full_location={'latitude':latitude,'longitude':longitude}
    # full_location_two={'latitude':latitude_two,'longitude':longitude_two}
    # z=haversine(full_location,full_location_two)
    # if not latitude and not longitude and not latitude_two and not longitude_two:
    #         raise forms.ValidationError('You have to write something!')
    # else:
    #     raise forms.Success(f'{z} is the closest distance')


#create a function and pass in a request as parameter, know what request 
#create a variable to capture instance of class Position with place and place_two
#call the haversine method
#render the template and display the output







