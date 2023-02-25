from django.shortcuts import render

from .models import Mags
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MagsSerializer


class MagsViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Mags.objects.all()
    # The serializer class for serializing output
    serializer_class = MagsSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]