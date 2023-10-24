from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        # Custom logic for listing users
        pass

    def create(self, request):
        # Custom logic for creating a user
        pass

    def retrieve(self, request, pk=None):
        # Custom logic for retrieving a user by ID
        pass

    def update(self, request, pk=None):
        # Custom logic for updating a user by ID
        pass

    def partial_update(self, request, pk=None):
        # Custom logic for partially updating a user by ID
        pass

    def destroy(self, request, pk=None):
        # Custom logic for deleting a user by ID
        pass




class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        # Custom logic for listing users
        pass

    def create(self, request):
        # Custom logic for creating a user
        pass

    def retrieve(self, request, pk=None):
        # Custom logic for retrieving a user by ID
        pass

    def update(self, request, pk=None):
        # Custom logic for updating a user by ID
        pass

    def partial_update(self, request, pk=None):
        # Custom logic for partially updating a user by ID
        pass

    def destroy(self, request, pk=None):
        # Custom logic for deleting a user by ID
        pass




class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        # Custom logic for listing users
        pass

    def create(self, request):
        # Custom logic for creating a user
        pass

    def retrieve(self, request, pk=None):
        # Custom logic for retrieving a user by ID
        pass

    def update(self, request, pk=None):
        # Custom logic for updating a user by ID
        pass

    def partial_update(self, request, pk=None):
        # Custom logic for partially updating a user by ID
        pass

    def destroy(self, request, pk=None):
        # Custom logic for deleting a user by ID
        pass
