from django.shortcuts import render, redirect, get_object_or_404
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

def editpatient(request, patient_id):
    patients = patient.objects.get(patient_id=patient_id)
    form = PatientForm(request.POST, instance = patients)
    if form.is_valid():
            form.save()
            return redirect('/viewpatients/')  # Redirect to the desired URL after updating the record.
    context = {'patients':patients, 'form':form}
    return render(request, 'editpatients.html', context)

def editward(request, ward_id):
    wards = ward.objects.get(ward_id=ward_id)
    form = WardForm(request.POST, instance = wards)
    if form.is_valid():
            form.save()
            return redirect('/viewwards/')  # Redirect to the desired URL after updating the record.
    context = {'ward':wards, 'form':form}
    return render(request, 'editward.html', context)

def viewwards(request, *args, **kwargs):
    wards = ward.objects.all()
    return render(request, "viewward.html", {'wards':wards,})

def viewpatients(request, *args, **kwargs):
    patients = patient.objects.all()
    return render(request, "viewpatients.html", {'patients':patients,})

def delete_patient(request, patient_id):
    patients = patient.objects.get(patient_id=patient_id)
    if request.method == 'POST':
        patients.delete()
        # Redirect to a success page or another appropriate URL
        return redirect('viewpatients')  #'viewpatients' is the name of the view to display the list of patients
    return render(request, 'delete_patient.html', {'patient': patients})

def delete_ward(request, ward_id):
    wards = ward.objects.get(ward_id=ward_id)
    if request.method == 'POST':
        wards.delete()
        # Redirect to a success page or another appropriate URL
        return redirect('viewwards')  #'viewwards' is the name of the view to display the list of wards
    return render(request, 'delete_ward.html', {'ward': wards})