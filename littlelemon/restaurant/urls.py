#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

path('api-token-auth/', obtain_auth_token)

