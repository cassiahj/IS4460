from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(max_length=11, primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    director = models.CharField(max_length=100)
    release_year = models.CharField(max_length=50)
    budget = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

class User(models.Model):
    user_id = models.IntegerField(max_length=11, primary_key=True, auto_created=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class role(models.Model):
    role_id = models.IntegerField(max_length=11, primary_key=True, auto_created=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=20)