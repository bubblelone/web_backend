from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from users import serializers



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


