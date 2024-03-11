import os

import django

from homework2.movie_app.user.models import User


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_app.settings')

django.setup()

#create list of movies and users and use a for loop to delete them all
users=User.objects.all()

for user in users:
    user.delete()

#add 10 movies and 3 users
User.objects.create(user_id=1, username="cassiah", password='password1', first_name="Cassiah", last_name="Nosack", email='cassiahjnosack@gmail.com')
