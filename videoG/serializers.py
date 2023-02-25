from .models import Mags
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Mags

        fields = ['id', 'title', 'rating', 'image','completed','notes',]