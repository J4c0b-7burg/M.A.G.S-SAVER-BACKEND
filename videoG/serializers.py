from .models import Videog
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class VideogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Videog

        fields = ['id', 'title', 'rating', 'image','completed','notes',]