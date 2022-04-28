from django.shortcuts import render,redirect
from django.urls import reverse


def home(request):
    if request.method == 'GET':
        return render(request, 'divccon/home.html', {})
        
    if request.method == 'POST':
        records = list(request.POST.values())[1::]
        request.session['firstname'] = records[0].upper()
        request.session['lastname'] = records[1].upper()
        request.session['pin'] = records[2].upper()
        return redirect('registration_two')

def registration_two(request):
    if request.method == 'GET':
        if not request.session['firstname'] or not request.session['lastname'] or not request.session['pin']:
            redirect('home')
        records = [request.session.get('firstname'),request.session.get('lastname')]
        return render(request, 'divccon/form2.html', {
            'records': records,
        })
    
    if request.method == 'POST':
        records = list(request.POST.values())[1::]    
