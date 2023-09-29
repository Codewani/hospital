from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.
def Patients(request, *args, **kwargs):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        name = request.POST['name']
        initials = request.POST['initials']
        sex = request.POST['sex']
        address = request.POST['address']
        post_code = request.POST['post_code']
        admission = request.POST['admission']
        DOB = request.POST['DOB']
        ward_id = request.POST['ward_id']
        next_of_kin = request.POST['next_of_kin']

        new_patient = patient(patient_id = patient_id, name = name, initials = initials, sex = sex, address = address, post_code = post_code, admission = admission, DOB = DOB, ward_id = ward_id, next_of_kin = next_of_kin, patients = patients)
    return render(request, "Patients.html", {})

def Wards(request, *args, **kwargs):
    return render(request, "ward.html", {})

def viewwards(request, *args, **kwargs):
    wards = ward.objects.all()
    return render(request, "viewward.html", {'wards':wards,})

def viewpatients(request, *args, **kwargs):
    patients = patient.objects.all()
    return render(request, "viewpatients.html", {'patients':patients,})