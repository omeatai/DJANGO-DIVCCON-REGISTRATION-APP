from django import forms
from .models import User, Province
from .choices import * 

class HomeForm(forms.Form):
    first_name = forms.CharField(
        label="Your First Name", 
        max_length=50, 
        min_length=2, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your First name',
            'class': 'form-control',
            }),
        error_messages = {
            "required": "Your firstname must not be empty",
            "max_length": "Please enter a shorter firstname",
            "min_length": "Please enter a longer firstname",
            })
    
    last_name = forms.CharField(
        label="Your Last Name", 
        max_length=50,
        min_length=2,  
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Last name',
            'class': 'form-control',
            }), 
        error_messages = {
            "required": "Your lastname must not be empty",
            "max_length": "Please enter a shorter lastname",
            "min_length": "Please enter a longer lastname",
            })
    
    password = forms.CharField(
        label="Your PIN", 
        max_length=6,
        min_length=6, 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your PIN',
            'class': 'form-control',
            }), 
        error_messages = {
            "required": "Your PIN must not be empty",
            "max_length": "Please enter a 6-digits PIN",
            "min_length": "Please enter a 6-digits PIN",
            })
    

class RegistrationTwoForm(forms.ModelForm):
    title = forms.CharField(
            label="Your Title", 
            max_length=50, 
            min_length=2, 
            required=True, 
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter your Title.... For example: Mr|Mrs|Revd|Rt Revd|Most Revd|Barr|Dr',
                'class': 'form-control',
                }),
            error_messages = {
                "required": "Your title must not be empty",
                "max_length": "Please enter a shorter title",
                "min_length": "Please enter a longer title",
                })
    
    phone = forms.CharField(
            label="Your Phone Number", 
            max_length=20, 
            min_length=8, 
            required=True, 
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter your Phone Number.... For example: +2348031111111',
                'class': 'form-control',
                }),
            error_messages = {
                "required": "Your phone number must not be empty",
                "max_length": "Please enter a shorter phone number",
                "min_length": "Please enter a longer phone number",
                }) 
    
    email = forms.EmailField(
            label="Your Email", 
            max_length=50, 
            min_length=5, 
            required=True, 
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter your Email.... For example: myemail@gmail.com',
                'class': 'form-control',
                }),
            error_messages = {
                "required": "Your email must not be empty",
                "max_length": "Please enter a shorter email",
                "min_length": "Please enter a longer email",
                })  
    
    sex = forms.ChoiceField(
            label="Your Sex",
            choices= SEX_CHOICES,
            required=True, 
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your Sex must not be empty",
                }) 
    
    anglican = forms.ChoiceField(
            label="Are you an Anglican?",
            choices= ANGLICAN_CHOICES,
            required=True, 
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your anglican field must not be empty",
                })  
    
    location = forms.ChoiceField(
            label="Where are you located?",
            choices= LOCATION_CHOICES,
            required=True, 
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your location field must not be empty",
                })         
    
    class Meta:
        model = User
        fields = ['title','phone','email','sex','anglican','location']


class RegistrationThreeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(RegistrationThreeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].label="Select your Province"
            self.fields[field].required=True
            self.fields[field].widget.attrs.update({
                'class': 'form-select form-select-sm'
            }) 
            self.fields[field].error_messages = {
            "required": "Your province field must not be empty",
            } 

    class Meta:
        model = User
        fields = ['province']  

