from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField()
    username=models.CharField()
    password=models.IntegerField
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=60)

class Movie(models.Model):
    movie_id=models.CharField()
    title=models.CharField()
    description=models.CharField()
    director=models.CharField()
    release_year=models.IntegerField()
    budget=models.IntegerField
    runtime=models.IntegerField
    rating=models.IntegerField
    genre=models.CharField(60)

