from django.db import models

class Languages(models.Model):
    name=models.CharField(max_length=100)
    paradigm=models.CharField(max_length=100)
