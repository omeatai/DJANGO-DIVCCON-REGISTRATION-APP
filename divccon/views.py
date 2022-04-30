# from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from django.core.mail import send_mail
from .forms import HomeForm, RegistrationTwoForm, RegistrationThreeForm


def home(request):
    if request.method == 'GET':
        form = HomeForm()
        return render(request, 'divccon/home.html', {
            'form': form,
        })
        
    if request.method == 'POST':
        form = HomeForm(request.POST)
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
            form = RegistrationTwoForm()    
            return render(request, 'divccon/form2.html', {
                'sessions': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('home')    
    
    if request.method == 'POST':
        form = RegistrationTwoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_three') 
        return render(request, 'divccon/form3.html', {
            'form': form,
        })

def registration_three(request):
    if request.method == 'GET':
        try:
            if not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location']:
                redirect('registration_two')
            form = RegistrationThreeForm()    
            return render(request, 'divccon/form3.html', {
                'sessions': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_two')    
    
    if request.method == 'POST':
        form = RegistrationThreeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).name.upper()
            return redirect('registration_four') 
        return render(request, 'divccon/form4.html', {
            'form': form,
        })


def registration_four(request):
    if request.method == 'GET':
        try:
            if not request.session['title'] or not request.session['phone'] or not request.session['email'] or not request.session['sex'] or not request.session['anglican'] or not request.session['location'] or not request.session['province']:
                redirect('registration_three')
            form = RegistrationThreeForm()    
            return render(request, 'divccon/form4.html', {
                'sessions': dict(request.session.items()),
                'form': form,   
            })
        except Exception:
            return redirect('registration_two')    
    
    if request.method == 'POST':
        form = RegistrationThreeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for key in data:
                request.session[key] = data.get(key).upper()
            return redirect('registration_four') 
        return render(request, 'divccon/form4.html', {
            'form': form,
        })





#send Email
# sender = "admin@divccon.com"
# subject = f"Registration for {first_name} {last_name}"
# message = f"<h2>From: {sender}</h2><br><h2>Congratulations {first_name} {last_name}, on your Registration!<br><h3>Your PIN is {pin}.</h2>"
# recipients = ['omeatai@gmail.com']
# send_mail(subject, message, sender, recipients)