from django.db import models

class Language(models.Model):
    name=models.CharField(max_length=100)
    paradigm=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
