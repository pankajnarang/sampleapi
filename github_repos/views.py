from django.shortcuts import render
from rest_framework import viewsets
from .models import githubRepo
from .serializers import repoSerializer

class   repoView(viewsets.ModelViewSet):
    queryset    =   githubRepo.objects.all()
    serializer_class    =   repoSerializer