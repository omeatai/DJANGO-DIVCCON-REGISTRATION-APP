from cProfile import label
from django import forms


class HomeForm(forms.Form):
    firstname = forms.CharField(
        label="Your First Name", 
        max_length=100, 
        required=True, 
        error_messages = {
            "invalid": "Please enter your first name",
            "required": "Your firstname must not be empty",
            "max_length": "Please enter a shorter firstname"
            })
    lastname = forms.CharField()
    pin = forms.CharField()
    

    