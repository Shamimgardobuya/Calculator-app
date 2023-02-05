#in order for a template to be seen each view is mapped to its url pattern
from django import views
from django.urls import path 
from .views import create_position,calculate_position,havepage
urlpatterns=[
    path('calculate/',create_position,name='calculate'),
    path('calculate/',create_position,name='calculate'),
    path('have/',havepage,name='have'),



    # path('resultt/',calculate_position,name='anss'),
    # path('result/',haversinee,name='ans'),
    # path('r/',calculate_position.calculating_the_haversine,name='a')
    


]