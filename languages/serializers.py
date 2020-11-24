from rest_framework import serializers
from .models import Language

class LanguageSerializers(serializers.ModelSerializers):
    class Meta:
        model=Language
        fields=('id','name','paradigm')