from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.IntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()


class Movie(models.Model):
    movie_id=models.IntegerField()
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    director=models.CharField(max_length=150)
    release_year=models.IntegerField()
    budget=models.IntegerField()
    runtime=models.IntegerField()
    rating=models.IntegerField()
    genre=models.CharField(max_length=40)

