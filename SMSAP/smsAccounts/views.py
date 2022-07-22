from django.shortcuts import render
from .serializers import profileSerializer
from rest_framework import viewsets
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = profileSerializer

