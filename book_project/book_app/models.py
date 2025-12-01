from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    
class Book(models.Model):
    title = models.CharField(max_length=64)
    publishing_year = models.IntegerField()
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)