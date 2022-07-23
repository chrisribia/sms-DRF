from django.shortcuts import render
from rest_framework import viewsets
from .models import ClassList, ClassMembers
from .serializers import ClassListSerializer, ClassMembersSerializer

class ClassListViewset(viewsets.ModelViewSet):
    queryset = ClassList.objects.all()
    serializer_class = ClassListSerializer


class ClassMembersViewset(viewsets.ModelViewSet):
    queryset = ClassMembers.objects.all()
    serializer_class = ClassMembersSerializer