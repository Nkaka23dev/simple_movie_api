from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializers 

class LanguageView(viewsets.ModelViewSet):
    querset=Language.objetcts.all()
    serilaizer_class=LanguageSerializers