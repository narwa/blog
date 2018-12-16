from django.shortcuts import render
from randompost.serializers import RandomPostSerializer
from rest_framework import viewsets
from .models import RandomPost

# Create your views here.
class RandomPostViewSet(viewsets.ModelViewSet):
    queryset = RandomPost.objects.all()
    serializer_class = RandomPostSerializer