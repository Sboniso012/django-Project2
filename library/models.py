from django.db import models
class Book(models.Model):
 title=models.CharField(max_length=200)
author=models.CharField(max_length=
100)
isbn=models.CharField(max_length=13,
unique=True)
published_date=models.DateField()
available=models.BooleanField(
default=True)
 def __str__(self):
  
return self.title
