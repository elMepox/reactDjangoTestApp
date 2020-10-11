from django.shortcuts import render
from .serializers import LeadSerializer
from .models import Lead
from rest_framework import generics


# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
