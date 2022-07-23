from rest_framework import serializers
from . models import ClassList, ClassMembers


class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ClassList
        fields = ('classNames','Teacher')

class ClassMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ClassMembers
        fields = ('classNames','classMemberReg')