#create a function that calculates the shortest distance between two spherical points using the Haversine method

#import math 
#create a variable for holdnig two points both lat and long
#using the radians function convert positions to degrees
#find differece between the latitude and longitudes
#multiply each with their cosines and sines
#use the earth's radius to get distance in kilometeres


from math import radians,asin,sqrt,cos,sin

def haversine(basigo_lat,basigo_long,London_lat,London_long):
    basigo_lat=radians(basigo_lat)
    basigo_long= radians(basigo_long) 
    London_lat=radians(London_lat)
    London_long=radians(London_long)
    difference_lat=basigo_lat-London_lat
    difference_long=basigo_long-London_long
    formula=sin(difference_lat/2)**2 + cos(basigo_lat)*cos(London_lat)*sin(difference_long/2)**2
    inverse=2*asin(sqrt(formula))
    
    earth_radius=6371
    distance=inverse*earth_radius
    print(distance)

haversine(53.32055555555556,-1.7297222222222221,53.31861111111111, -1.6997222222222223)



