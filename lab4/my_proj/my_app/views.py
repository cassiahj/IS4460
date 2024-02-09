from django.views import View
from django.shortcuts import render, redirect
from . import my_functions
from . import my_objects

def title_name(the_name: str):
    return the_name.title()


class HomePageView(View):
    def get(self, request):

        my_name = "CAssIah"
        new_name = title_name(my_name)

        names = ['lUIse', 'GabrIel', 'MaY']

        fixed_names = my_functions.fix_names_list(names)

        car1 = my_objects.Car(make="Toyota",model="4Runner",year=2000,color='green',sound="honk honks")
        car2 = my_objects.Car(make='Honda',model='civic',year=2012,color='purple',sound="beep beepers")

        motorcycle1 = my_objects.Motorcycle(make='Kawasaki',model='Z1000',year=2015,color='black',sound='meep meep')

        context = {'hi':'hello world!', 'name':new_name, 'orig_name':my_name, 'names': names, 'fixed_names': fixed_names,
                   'car1': car1, 'car2': car2, 'motorcycle1': motorcycle1
                   }

        return render(request, 'my_app/index.html', context)