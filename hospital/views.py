from tokenize import Special
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Appointment, Doctor, Patient, Staff, Prescription

# Create your views here.


def About(request):
    return render(request, 'about.html')


def Home(request):
    return render(request, 'home.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        print(u)
        print(p)
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'login.html', {'error': error})


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('login')


def Dashboard(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'dashboard.html')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=m, special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc': doc}
    return render(request, 'view_patient.html', d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Patient.objects.get(id=pid)
    doctor.delete()
    return redirect('view_patient')


def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appointment.objects.all()
    d = {'doc': doc}
    return render(request, 'view_appointment.html', d)


def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.get(id=pid)
    app.delete()
    return redirect('view_appointment')


def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        n = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=n).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(
                Doctor=doctor, Patient=patient, date=da, time=t)
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appointment.html', d)


def View_Staff(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Staff.objects.all()
    d = {'doc': doc}
    return render(request, 'view_staff.html', d)


def Delete_Staff(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    stff = Staff.objects.get(id=pid)
    stff.delete()
    return redirect('view_staff')


def Add_Staff(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Staff.objects.create(name=n, mobile=m, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_staff.html', d)


def View_Prescription(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Prescription.objects.all()
    d = {'doc': doc}
    return render(request, 'view_prescription.html', d)


def Delete_Prescription(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Prescription.objects.get(id=pid)
    app.delete()
    return redirect('view_prescription')


def Add_Prescription(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    staff1 = Staff.objects.all()

    if request.method == 'POST':
        n = request.POST['doctor']
        p = request.POST['patient']
        s = request.POST['staff']
        da = request.POST['date']
        t = request.POST['time']
        a = request.POST['advice']
        doctor = Doctor.objects.filter(name=n).first()
        patient = Patient.objects.filter(name=p).first()
        staff = Staff.objects.filter(name=s).first()
        try:
            Prescription.objects.create(
                Doctor=doctor, Patient=patient, Staff=staff, date=da, time=t, advice=a)
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'staff': staff1, 'error': error}
    return render(request, 'add_prescription.html', d)
