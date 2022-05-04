# from django.http import HttpResponseRedirect
from dataclasses import fields
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic.edit import CreateView
from . import forms
from . import choices
from .models import User


def home(request):
    if request.method == 'GET':
        form = forms.HomeForm()
        return render(request, 'divccon/home.html', {
            'form': form,
        })
    elif request.method == 'POST':
        form = forms.HomeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_two')
        return render(request, 'divccon/home.html', {
            'form': form,
        })


def registration_two(request):
    if request.method == 'GET':
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password']:
                redirect('home')
            form = forms.RegistrationTwoForm()    
            return render(request, 'divccon/form2.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('home')    
    
    if request.method == 'POST':
        form = forms.RegistrationTwoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_three') 
        return render(request, 'divccon/form2.html', {
            'form': form,
        })

def registration_three(request):
    if request.method == 'GET':
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location']:
                redirect('registration_two')
            form = forms.RegistrationThreeForm()    
            return render(request, 'divccon/form3.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_two')    
    
    if request.method == 'POST':
        form = forms.RegistrationThreeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_four') 
        return render(request, 'divccon/form3.html', {
            'form': form,
        })


def registration_four(request):
    if request.method == 'GET':
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province']:
                redirect('registration_three')
            form = forms.DioceseForm() 
            #Logic for Dioceses
            if request.session['province'] == "INSTITUTION":
                form.fields['diocese'].choices = choices.INSTITUTION_DIOCESE_CHOICES 
            elif request.session['province'] == "ABA":
                form.fields['diocese'].choices = choices.ABA_DIOCESE_CHOICES 
            elif request.session['province'] == "ABUJA":
                form.fields['diocese'].choices = choices.ABUJA_DIOCESE_CHOICES 
            elif request.session['province'] == "BENDEL":
                form.fields['diocese'].choices = choices.BENDEL_DIOCESE_CHOICES 
            elif request.session['province'] == "ENUGU":
                form.fields['diocese'].choices = choices.ENUGU_DIOCESE_CHOICES 
            elif request.session['province'] == "IBADAN":
                form.fields['diocese'].choices = choices.IBADAN_DIOCESE_CHOICES 
            elif request.session['province'] == "JOS":
                form.fields['diocese'].choices = choices.JOS_DIOCESE_CHOICES 
            elif request.session['province'] == "KADUNA":
                form.fields['diocese'].choices = choices.KADUNA_DIOCESE_CHOICES     
            elif request.session['province'] == "KWARA":
                form.fields['diocese'].choices = choices.KWARA_DIOCESE_CHOICES     
            elif request.session['province'] == "LAGOS":
                form.fields['diocese'].choices = choices.LAGOS_DIOCESE_CHOICES     
            elif request.session['province'] == "LOKOJA":
                form.fields['diocese'].choices = choices.LOKOJA_DIOCESE_CHOICES     
            elif request.session['province'] == "NIGERDELTA":
                form.fields['diocese'].choices = choices.NIGERDELTA_DIOCESE_CHOICES     
            elif request.session['province'] == "OFTHENIGER":
                form.fields['diocese'].choices = choices.OFTHENIGER_DIOCESE_CHOICES 
            elif request.session['province'] == "ONDO":
                form.fields['diocese'].choices = choices.ONDO_DIOCESE_CHOICES  
            elif request.session['province'] == "OWERRI":
                form.fields['diocese'].choices = choices.OWERRI_DIOCESE_CHOICES  
            elif request.session['province'] == "CANA":
                form.fields['diocese'].choices = choices.CANA_DIOCESE_CHOICES                      
            
            request.session['choice'] = form.fields['diocese'].choices         
            return render(request, 'divccon/form4.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_three')    
    
    if request.method == 'POST':
        form = forms.DioceseForm(request.POST)
        form.fields['diocese'].choices = request.session['choice']
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_five') 
        return render(request, 'divccon/form4.html', {
            'form': form,
        })


def registration_five(request):
    if request.method == 'GET':
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province'] or not request.session['diocese']:
                redirect('registration_four')
            form = forms.ChurchForm()    
            return render(request, 'divccon/form5.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_four')    
    
    if request.method == 'POST':
        form = forms.ChurchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_six') 
        return render(request, 'divccon/form5.html', {
            'form': form,
        })


def registration_six(request):
    if request.method == 'GET':
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province'] or not request.session['diocese'] or not request.session['church']:
                redirect('registration_six')
            form = forms.DesignationForm()    
            return render(request, 'divccon/form6.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_five')    
    
    if request.method == 'POST':
        form = forms.DesignationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_seven') 
        return render(request, 'divccon/form6.html', {
            'form': form,
        })



class PhotoCreateView(CreateView):
    model = User
    form_class = forms.PhotoForm
    # fields = ["photo"]
    template_name = "divccon/form7.html"
    success_url = reverse_lazy('registration_seven')

    def get(self, request):
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province'] or not request.session['diocese'] or not request.session['church'] or not request.session['designation']:
                redirect('registration_seven')
            form = forms.PhotoForm()    
            return render(request, 'divccon/form7.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_six') 
    
    def post(self, request):
        photo_image = request.FILES["photo"]
        photo_name = photo_image.name
        photo_size = photo_image.size
        photo_type = photo_image.content_type
        first_name = request.session['first_name']
        last_name = request.session['last_name']
        name = f"{first_name}_{last_name}_{photo_name}"
        
        form = forms.PhotoForm(request.POST, request.FILES) 
        
        if form.is_valid():
            photo_image.name = name
            instance = User()
            instance.photo=photo_image
            instance.username = name
            instance.save()

            request.session['photo'] = name  
            return redirect('registration_seven')
        return render(request, 'divccon/form7.html', {
            'form': form,
        })    



# def registration_seven(request):
#     if request.method == 'GET':
#         try:
#             if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province'] or not request.session['diocese'] or not request.session['church'] or not request.session['designation']:
#                 redirect('registration_seven')
#             form = forms.PhotoForm()    
#             return render(request, 'divccon/form7.html', {
#                 'sessions': request.session,
#                 'sessions_view': dict(request.session.items()),
#                 'form': form,   
#             })
#         except Exception:
#             return redirect('registration_six') 

    # def store_file(file,name):
    #     with open(f"divccon/media/{name}","wb+") as dest:
    #         for chunk in file.chunks():
    #             dest.write(chunk)      
    
    # if request.method == 'POST':
    #     photo_image = request.FILES["photo"]
    #     photo_name = photo_image.name
    #     photo_size = photo_image.size
    #     photo_type = photo_image.content_type
    #     first_name = request.session['first_name']
    #     last_name = request.session['last_name']
    #     name = f"{first_name}_{last_name}_{photo_name}"
        
    #     form = forms.PhotoForm(request.POST, request.FILES) 
        
    #     if form.is_valid():
    #         # store_file(photo_image, name)
    #         photo_image.name = name
    #         instance = User()
    #         instance.photo=photo_image
    #         instance.username = name
    #         instance.save()
            
    #         print(photo_name, photo_size, photo_type)
    #         request.session['photo'] = name  
    #         return redirect('registration_seven')
    #     return render(request, 'divccon/form7.html', {
    #         'form': form,
    #     })
        
        
        # if not photo_size <= 5000000:
        #     raise Exception("Image size is too large: more than 5MB. Try Again!") 
        # if not photo_type in ('image/jpeg','image/jpg','image/png'):
        #     raise Exception("Image Type is not among these: PNG, JPG or JPEG. Try Again!") 

        


















#send Email
# sender = "admin@divccon.com"
# subject = f"Registration for {first_name} {last_name}"
# message = f"<h2>From: {sender}</h2><br><h2>Congratulations {first_name} {last_name}, on your Registration!<br><h3>Your PIN is {pin}.</h2>"
# recipients = ['omeatai@gmail.com']
# send_mail(subject, message, sender, recipients)