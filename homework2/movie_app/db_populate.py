import os

import django

from user.models import User,Movie
#,getUserData
#import getUserData from user.models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_app.settings')

django.setup()


def getUserData(username):
    for result in User.objects.raw("Select * from user_user where username = %s", [username]):
        print(result)


#create list of movies and users and use a for loop to delete them all
users=User.objects.all()
movies=Movie.objects.all()

for user in users:
    user.delete()
for movie in movies:
    movie.delete()

#add 10 movies and 3 users
user1=User.objects.create(user_id=1, username="cassiah", password='password1', first_name="Cassiah", last_name="Nosack", email='cassiahjnosack@gmail.com')
user2=User.objects.create(user_id=2, username="matt", password='password2', first_name="Matt", last_name="Pecsok", email='mattpecsok@gmail.com')
user3=User.objects.create(user_id=3, username="priyanker", password='password3', first_name="Priyanker", last_name="TA", email='priyankerTA@gmail.com')

movie1=Movie.objects.create(movie_id=1, title='Dune', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='adventure')
movie2=Movie.objects.create(movie_id=2, title='Dune 2', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='adventure')
movie3=Movie.objects.create(movie_id=3, title='Inside Out', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='kid')
movie4=Movie.objects.create(movie_id=4, title='Inside Out 2', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='kid')
movie5=Movie.objects.create(movie_id=5, title='Avatar', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='adventure')
movie6=Movie.objects.create(movie_id=6, title='Avatar: way of water', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='adventure')
movie7=Movie.objects.create(movie_id=7, title='Barbie', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='adventure')
movie8=Movie.objects.create(movie_id=8, title='Tenet', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='adventure')
movie9=Movie.objects.create(movie_id=9, title='Oppenhiemer', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='mind-bending')
movie10=Movie.objects.create(movie_id=10, title='Kung Fu Panda', description='alkdjflajldfjlaksdfj', director='director', release_year=2020, budget=4000000, runtime=300, 
                            rating=9, genre='kid')


# Django QuerySet statements for Movie
moviesList=Movie.objects.all()
#dunes=Movie.objects.filter(name_startswith=("Dune"))
#barb=Movie.objects.filter(name='Barbie')
movie1.name='KungFu Pand 4'
movie9.delete()


#sql statement
getUserData('cassiah')
