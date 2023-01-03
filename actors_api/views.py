from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ActorSerializer
from .models import Actor

class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer

class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer
