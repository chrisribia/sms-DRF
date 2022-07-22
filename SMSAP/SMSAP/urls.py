import profile
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from smsAccounts.views import ProfileViewSet


router = DefaultRouter()
router.register("",ProfileViewSet,basename="profile")


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('profile/', include(router.urls)),
]
