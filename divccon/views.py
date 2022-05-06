from re import I
from django.shortcuts import render,redirect
# from django.http import HttpResponse, HttpResponseRedirect, response
# from django.urls import reverse, reverse_lazy
# from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView
from . import forms
from . import choices
from .models import User


class HomeCreateView(CreateView):
    model = User
    form_class = forms.HomeForm
    template_name = 'divccon/home.html'
    
    def post(self, request): 
        try:
            # messages.success(request,'Welcome to Divccon!')       
            form = forms.HomeForm(request.POST)
            request.session.flush()
            if form.is_valid():
                data = form.cleaned_data
                request.session['first_name'] = data.get('first_name').upper()
                request.session['last_name'] = data.get('last_name').upper()
                request.session['password'] = data.get('password')
                
                # passw = data.get('password')
                # for i in User.objects.all():
                #     print(check_password(passw, i.password))
                    
                return redirect('registration_two')
            return render(request, 'divccon/home.html', {
                'form': form,
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('home')  

class RegistrationTwoCreateView(CreateView):
    model = User
    form_class = forms.RegistrationTwoForm
    template_name = 'divccon/form2.html'
    
    def get(self, request):
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password']:
                redirect('home')
            form = forms.RegistrationTwoForm()    
            return render(request, 'divccon/form2.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('home')     
    
    def post(self, request): 
        try:   
            form = forms.RegistrationTwoForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                for key in data:
                    request.session[key] = data.get(key).upper()
                if request.session['anglican'] == 'NON-ANGLICAN' or request.session['location'] == 'ABROAD':
                    request.session['province'] = "NONE"
                    request.session['diocese'] = "NONE"
                    request.session['church'] = "NONE"
                    return redirect('registration_six')   
                return redirect('registration_three')     
                    
            return render(request, 'divccon/form2.html', {
                'form': form,
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_two')  
                

class RegistrationThreeCreateView(CreateView):
    model = User
    form_class = forms.RegistrationThreeForm
    template_name = 'divccon/form3.html'
    
    def get(self, request):
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location']:
                redirect('registration_two')
            form = forms.RegistrationThreeForm()    
            return render(request, 'divccon/form3.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_two')    
    
    def post(self, request): 
        try:   
            form = forms.RegistrationThreeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                for key in data:
                    request.session[key] = data.get(key).upper()
                return redirect('registration_four') 
            return render(request, 'divccon/form3.html', {
                'form': form,
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_three')      


class DioceseFormCreateView(CreateView):
    PROVINCES = {
        "INSTITUTION": choices.INSTITUTION_DIOCESE_CHOICES, 
        "ABA": choices.ABA_DIOCESE_CHOICES,
        "ABUJA": choices.ABUJA_DIOCESE_CHOICES,
        "BENDEL": choices.BENDEL_DIOCESE_CHOICES,
        "ENUGU": choices.ENUGU_DIOCESE_CHOICES,
        "IBADAN": choices.IBADAN_DIOCESE_CHOICES,
        "JOS": choices.JOS_DIOCESE_CHOICES,
        "KADUNA": choices.KADUNA_DIOCESE_CHOICES,
        "KWARA": choices.KWARA_DIOCESE_CHOICES,
        "LAGOS": choices.LAGOS_DIOCESE_CHOICES,
        "LOKOJA": choices.LOKOJA_DIOCESE_CHOICES,
        "NIGERDELTA": choices.NIGERDELTA_DIOCESE_CHOICES,
        "OFTHENIGER": choices.OFTHENIGER_DIOCESE_CHOICES,
        "ONDO": choices.ONDO_DIOCESE_CHOICES,
        "OWERRI": choices.OWERRI_DIOCESE_CHOICES,
        "CANA": choices.CANA_DIOCESE_CHOICES,
        "NONE": choices.NONE_DIOCESE_CHOICES,
    }
    
    model = User
    form_class = forms.DioceseForm
    template_name = 'divccon/form4.html'
    
    def get(self, request):
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province']:
                redirect('registration_three')
            form = forms.DioceseForm() 
            form.fields['diocese'].choices = self.PROVINCES[request.session['province']]                 
            request.session['choice'] = form.fields['diocese'].choices         
            return render(request, 'divccon/form4.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_three')   
    
    def post(self, request): 
        try:   
            form = forms.DioceseForm(request.POST)
            form.fields['diocese'].choices = request.session['choice']
            if form.is_valid():
                data = form.cleaned_data
                for key in data:
                    request.session[key] = data.get(key).upper()
                if request.session['diocese'] != 'ABUJA':
                    request.session['church'] = "NONE"
                    return redirect('registration_six') 
                return redirect('registration_five') 
            return render(request, 'divccon/form4.html', {
                'form': form,
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_four')     
            


class ChurchCreateView(CreateView):
    model = User
    form_class = forms.ChurchForm
    template_name = 'divccon/form5.html'
    
    def get(self, request):
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province'] or not request.session['diocese']:
                redirect('registration_four')
            form = forms.ChurchForm()    
            return render(request, 'divccon/form5.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_four') 
    
    def post(self, request):
        try:    
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
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_five')          


class DesignationCreateView(CreateView):
    model = User
    form_class = forms.DesignationForm
    template_name = 'divccon/form6.html'
    
    def get(self, request):
        try:
            if not request.session['first_name'] or not request.session['last_name'] or not request.session['password'] or not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province'] or not request.session['diocese'] or not request.session['church']:
                redirect('registration_five')
            form = forms.DesignationForm()    
            return render(request, 'divccon/form6.html', {
                'sessions': request.session,
                'sessions_view': dict(request.session.items()),
                'form': form,   
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_five')     
    
    def post(self, request): 
        try:   
            form = forms.DesignationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                for key in data:
                    request.session[key] = data.get(key).upper()
                return redirect('registration_seven') 
            return render(request, 'divccon/form6.html', {
                'form': form,
            })
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
            return redirect('registration_six')     



class PhotoCreateView(CreateView):
    model = User
    form_class = forms.PhotoForm
    template_name = "divccon/form7.html"
    # fields = ["photo"]
    # context_object_name = "photos"
    # success_url = reverse_lazy('registration_seven')

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
        except Exception as err:
            messages.error(request,f'There was an Error - {err}') 
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
        
        if  photo_size > 5000000:
            messages.error(request,'Your Image is too large. Must be less than 5MB. Try Again!') 
            return redirect('registration_seven')
        
        if  not photo_type in {'image/jpeg','image/jpg','image/png'}:
            messages.error(request,'Image Type is not among these: PNG, JPG or JPEG. Try Again!') 
            return redirect('registration_seven')
        
        if form.is_valid():
            photo_image.name = name
            instance = User()
            instance.username = name
            instance.first_name = request.session['first_name']
            instance.last_name = request.session['last_name']
            instance.set_password(request.session['password'])
            instance.title = request.session['title']
            instance.phone = request.session['phone']
            instance.email = request.session['email']
            instance.sex = request.session['sex']
            instance.anglican = request.session['anglican']
            instance.location = request.session['location']
            instance.province = request.session['province']
            instance.diocese = request.session['diocese']
            instance.church = request.session['church']
            instance.designation = request.session['designation']
            instance.committee = "NONE"
            instance.photo=photo_image
            instance.save()
            
            request.session['photo'] = name  
            messages.success(request,f'Congratulations! You are registered.') 
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