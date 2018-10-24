from django.db import models

# Create your models here.
class Document(models.Model):
    _user = models.CharField(max_length=150)
    _file_path = models.CharField(max_length=1000)
    _data = models.BinaryField(blank=True)
