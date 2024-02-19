from django.shortcuts import render
from django.views import View


class ThankYouPageView(View):
    
    template_name: 'lab5/thanks.html'

    def get(self, request):

        my_name="Cassiah Nosack"

        return render(request, self.template_name,{'my_name':my_name})