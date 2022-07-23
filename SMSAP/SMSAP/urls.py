import profile
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from smsAccounts.views import ProfileViewSet
from classManagement.views import ClassMembersViewset, ClassListViewset


router = DefaultRouter()
router.register("prof",ProfileViewSet,basename="profile")
router.register("classList",ClassListViewset,basename="classLists")
router.register("classMember",ClassMembersViewset,basename="classMembers")


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('profile/', include(router.urls)),
    path('classLists/', include(router.urls)),
    path('classMembers/', include(router.urls)),
]
