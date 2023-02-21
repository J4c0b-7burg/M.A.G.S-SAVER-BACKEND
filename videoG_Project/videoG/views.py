from django.shortcuts import render

from .models import Videog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import VideogSerializer


class VideogViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Videog.objects.all()
    # The serializer class for serializing output
    serializer_class = VideogSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]