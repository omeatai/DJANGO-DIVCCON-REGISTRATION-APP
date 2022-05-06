from django import forms
from .models import User
from .choices import * 
from django.core.validators import RegexValidator

alphabets = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabet characters are allowed.')

#Home-Form 1
class HomeForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Your First Name", 
        validators=[alphabets],
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
        validators=[alphabets],
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
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your PIN',
            'class': 'form-control',
            }), 
        error_messages = {
            "required": "Your PIN must not be empty",
            "max_length": "Please enter a 6-digits PIN",
            "min_length": "Please enter a 6-digits PIN",
            })
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'password']



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

#PROVINCE

class RegistrationThreeForm(forms.ModelForm):
    province = forms.ChoiceField(
            label="Select your Province",
            choices= PROVINCE_CHOICES,
            required=True, 
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your province field must not be empty",
                })  

    class Meta:
        model = User
        fields = ['province']  


#DIOCESE

class DioceseForm(forms.ModelForm):
    diocese = forms.ChoiceField(
            label="Select your Diocese",
            required=True, 
            # choices= ABUJA_DIOCESE_CHOICES,
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your Diocese field must not be empty",
                })  

    class Meta:
        model = User
        fields = ['diocese']  


#CHURCH
        
class ChurchForm(forms.ModelForm):
    church = forms.ChoiceField(
            label="Select your Church",
            choices= CHURCH_CHOICES,
            required=True, 
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your Church field must not be empty",
                })  

    class Meta:
        model = User
        fields = ['church']  
        
        
#DESIGNATION
        
class DesignationForm(forms.ModelForm):
    designation = forms.ChoiceField(
            label="Select your Designation",
            choices= DESIGNATION_CHOICES,
            required=True, 
            widget=forms.Select(attrs={
                'class': 'form-select form-select-sm',
                }),
            error_messages = {
                "required": "Your Designation field must not be empty",
                })  

    class Meta:
        model = User
        fields = ['designation']        
        

#PHOTO

class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(
            label="Your Photo Image", 
            required=True, 
            widget=forms.FileInput(attrs={
                'placeholder': 'Upload your Image',
                'type': 'file',
                'title': 'Click here to Upload',
                'style': "color: red",
                'class': 'form-control form-control-lg',
                }),
            error_messages = {
                "required": "Your image field must not be empty",
                })  

    class Meta:
        model = User
        fields = ['photo']      
        
        
        