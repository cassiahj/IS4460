from urllib import request
from django import forms
from django.shortcuts import render

class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=60)
    review_area= forms.MultipleChoiceField(choices=[('food','Food'),('srvc','Service'),('amb','Ambiance')],widget=forms.CheckboxSelectMultiple)  


    def clean_my_message(self):

        if self.is_valid():
            my_message: str = self.cleaned_data.get('my_message')
            review_area: str = self.cleaned_data.get('review_area')

            #if 'srvc' in review_area:
            #    service_selected = True
        
        if "awful" in my_message:
            raise forms.ValidationError(f"We don't take bad reviews like:'{my_message}'")
        
        return {'my_message':my_message
                                                   #,'service_selected':service_selected
                                                   }

