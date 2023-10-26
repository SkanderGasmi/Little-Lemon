from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   Menu
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

   #queryset = MenuItem.objects.all()
   #serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]