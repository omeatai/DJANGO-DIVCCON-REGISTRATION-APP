# from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from .forms import HomeForm
from django.core.mail import send_mail


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
            firstname = data['firstname'].upper()
            lastname = data['lastname'].upper()
            pin = data['pin'].upper()
            request.session['firstname'] = firstname
            request.session['lastname'] = lastname
            request.session['pin'] = pin
            
            sender = "admin@divccon.com"
            subject = f"Registration for {firstname} {lastname}"
            message = f"<h2>From: {sender}</h2><br><h2>Congratulations {firstname} {lastname}, on your Registration!<br><h3>Your PIN is {pin}.</h2>"
            recipients = ['omeatai@gmail.com']
            send_mail(subject, message, sender, recipients)
            
            return redirect('registration_two')
        return render(request, 'divccon/home.html', {
            'form': form,
        })


def registration_two(request):
    if request.method == 'GET':
        if not request.session['firstname'] or not request.session['lastname'] or not request.session['pin']:
            redirect('home')
        records = { 
            'firstname': request.session.get('firstname'),
            'lastname': request.session.get('lastname'),
            'pin': request.session.get('pin')
            }
        return render(request, 'divccon/form2.html', {
            'records': records,
        })
    
    if request.method == 'POST':
        return redirect('home')   
