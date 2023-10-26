from rest_framework import serializers 
from .models import * 


from django.contrib.auth.models import User
from rest_framework import serializers


#define Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


#define Serializer class for User model
class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'


#define Serializer class for User model
class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'

