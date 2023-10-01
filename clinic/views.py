from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

from .models import *
# Create your views here.
def Patients(request, *args, **kwargs):
    form = PatientForm()
    if request.method == 'POST':
        print(request.POST)
        form = PatientForm(request.POST)
        if form.is_valid():
            print("valid")    
            try:  
                form.save()  
                return redirect('/patient')  
            except:  
                pass 
        else:
            print("not valid")  
            form = PatientForm()  

    wards = ward.objects.all()
    context = {'wards':wards, 'form':form}
    return render(request, "Patients.html", context)

def Wards(request, *args, **kwargs):
    form = WardForm()
    if request.method == 'POST':
        print(request.POST)
        form = WardForm(request.POST)
        if form.is_valid():
            print("valid")    
            try:  
                form.save()  
                return redirect('/ward')  
            except:  
                pass 
        else:
            print("not valid")  
            form = WardForm()  

    wards = ward.objects.all()
    context = {'wards':wards, 'form':form}
    return render(request, "ward.html", context)

def viewwards(request, *args, **kwargs):
    wards = ward.objects.all()
    return render(request, "viewward.html", {'wards':wards,})

def viewpatients(request, *args, **kwargs):
    patients = patient.objects.all()
    return render(request, "viewpatients.html", {'patients':patients,})