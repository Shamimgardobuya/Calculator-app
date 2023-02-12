from django.forms import ModelForm
from .models import Place,Position

class PositionForm(ModelForm):
    class Meta:
        model=Position 
        fields=['latitude','longitude','latitude_two','longitude_two','speed_of_car']
    
# class PlaceForm(ModelForm):
#     class Meta:
#         model=Place
#         fields='__all__'