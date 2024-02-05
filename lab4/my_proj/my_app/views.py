from django.views import View
from django.shortcuts import render, redirect

def title_name(the_name: str):
    return the_name.title()


class HomePageView(View):
    def get(self, request):

        my_name = "CAssIah"
        new_name = title_name(my_name)

        names = ['Luise', 'Gabriel', 'May']

        context = {'hi':'hello world!', 'name':new_name, 'orig_name':my_name, 'names': names}

        return render(request, 'my_app/index.html', context)