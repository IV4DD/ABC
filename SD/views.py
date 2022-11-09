from .forms import CoworkerForm, PatientForm, PaymentForm, DoctorForm, ProcedurForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    data = {

            }
    return render(request,
                'SD/home.html',
                data)

def next_update(request):
    data = {
            }
    return render(request,
                'SD/next_update.html',
                data)

def dashboard(request):
    data = {
            }
    return render(request,
                  'SD/dashboard.html',
                  data)

def coworker_create(request):
    form = CoworkerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Данные зарегистрированы успешно!")
        return HttpResponseRedirect('/coworker_create')
    data = {
        'form': form,
    }
    return render(request,
                  'SD/coworker/coworker_create.html',
                  data)

def patient_create(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Данные зарегистрированы успешно!")
        return HttpResponseRedirect('/patient_create')
    data = {
        'form': form,
    }
    return render(request,
                  'SD/patient/patient_create.html',
                  data)

def payment_create(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Данные зарегистрированы успешно!")
        return HttpResponseRedirect('/payment_create')
    data = {
        'form': form,
            }
    return render(request,
                  'SD/payment/payment_create.html',
                  data)

def doctor_create(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Данные зарегистрированы успешно!")
        return HttpResponseRedirect('/doctor_create')
    data = {
        'form': form,
            }
    return render(request,
                  'SD/doctor/doctor_create.html',
                  data)

def procedur_create(request):
    form = ProcedurForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Данные зарегистрированы успешно!")
        return HttpResponseRedirect('/procedur_create')
    data = {
        'form': form,
    }
    return render(request,
                  'SD/procedur/procedur_create.html',
                  data)

def coworker_personal_page(request):
    data = {
            }
    return render(request,
                  'SD/coworker/coworker_personal_page.html',
                  data)

'''
from .forms import CandidateForm, PatientForm

from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from registration.decorators import unauthenticated_user, allowed_users, admin_only

from .filters import DoctorFilter, ProcedurFilter




@login_required(login_url='login')
def home(request):

    data = {
            }
    return render(request,
                'main/worker_view.html',
                data)


@login_required(login_url='login')
def candidate_view(request):
    form = CandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Данные зарегистрированы успешно!")
        return HttpResponseRedirect('/')
    data = {
        'form': form,
    }
    return render(request,
                'TEMPORARY/worker_view.html',
                data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def dashboard(request):
    patients = Patient.objects.all()
    payments = Payment.objects.all()
    doctors = Doctor.objects.all()
    total_patients = patients.count()
    total_payments = payments.count()
    total_doctors = doctors.count()

    data = {
            'patients': patients,
            'payments': payments,
            'doctors': doctors,
            'total_patients': total_patients,
            'total_payments': total_payments,
            'total_doctors': total_doctors
            }

    return render(request,
                'main/dashboard.html',
                data)


                )

# Patient (need for Database)
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    data = {
        'patient': patient,
    }
    if patient != None:
        return render(request, 'dm_patients/patient_update.html', data)

# Patient update
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def patient_update(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id= request.POST.get('id'))
        if patient != None:

            patient.first_name = request.POST.get('first_name')
            patient.surname = request.POST.get('surname')
            patient.middle_name = request.POST.get('middle_name')
            patient.phone = request.POST.get('phone')
            patient.iin = request.POST.get('iin')
            patient.gender = request.POST.get('gender')
            patient.age = request.POST.get('age')
            patient.note = request.POST.get('note')
            patient.save()

            messages.success(request, 'Данные пациента изменены!')
            return HttpResponseRedirect('patients_database')

# Patient Personal page
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def patient_personal_page(request, pk):
    patients = Patient.objects.get(id=pk)

    payments = patients.payment_set.all()

    data = {
            'patients': patients,
            'payments': payments,
            }
    return render(request,
                  'dm_patients/patient_personal_page.html',
                  data)

# Patient Delete
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def patient_delete(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patients_database')

    data = {'item': patient, }

    return render(request, 'dm_patients/patient_delete.html',
                  data)

# Patient Database
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def patients_database(request):

    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(first_name__icontains=q) | Q(surname__icontains=q) | Q(middle_name__icontains=q) | Q(
                phone__icontains=q) | Q(iin__icontains=q) | Q(note__icontains=q)
        ).order_by('-date_created')

    else:
        all_patient_list = Patient.objects.all().order_by('-date_created')
    paginator = Paginator(all_patient_list, 15)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    data = {
        'patients': all_patient,
    }
    return render(request,
                  'dm_patients/patients_database.html',
                  data)



# Doctor Create
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def doctor_create(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('surname') and request.POST.get('phone') and request.POST.get('percent') and request.POST.get('department') and request.POST.get('email') and request.POST.get('birthday'):
            doctor = Doctor()
            doctor.first_name = request.POST.get('first_name')
            doctor.middle_name = request.POST.get('middle_name')
            doctor.surname = request.POST.get('surname')
            doctor.phone = request.POST.get('phone')
            doctor.percent = request.POST.get('percent')
            doctor.department = request.POST.get('department')
            doctor.email = request.POST.get('email')
            doctor.birthday = request.POST.get('birthday')
            doctor.save()
            messages.success(request, 'Врач успешно зарегистрирован!')
            return HttpResponseRedirect('doctors_database')
    else:
            return render(request,
                          'dm_doctors/doctor_create.html',
                          )

# Doctor (need for Database)
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def doctor(request, doctor_id):
    doctor = Doctor.objects.get(id = doctor_id)
    data = {
        'doctor': doctor,
    }
    if doctor != None:
        return render(request, "dm_doctors/doctor_update.html", data)

# Doctor update
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def doctor_update(request):
    if request.method == 'POST':
        doctor = Doctor.objects.get(id= request.POST.get('id'))
        if doctor != None:

            doctor.first_name = request.POST.get('first_name')
            doctor.middle_name = request.POST.get('middle_name')
            doctor.surname = request.POST.get('surname')
            doctor.phone = request.POST.get('phone')
            doctor.percent = request.POST.get('percent')
            doctor.department = request.POST.get('department')
            doctor.email = request.POST.get('email')
            doctor.birthday = request.POST.get('birthday')
            doctor.save()

            messages.success(request, 'Данные врача изменены!')
            return HttpResponseRedirect('doctors_database')

# Doctor Personal page
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def doctor_personal_page(request, pk):
    doctors = Doctor.objects.get(id=pk)

    payments = doctors.payment_set.all()
    payment_count = payments.count()

    doctorfilter = DoctorFilter(request.GET, queryset=payments)
    payments = doctorfilter.qs

    data = {'doctors': doctors,
            'payments': payments,
            'payment_count': payment_count,
            'doctorfilter': doctorfilter,
    }
    return render(request,
                  'dm_doctors/doctor_personal_page.html',
                  data)

# Doctor Database
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def doctor_delete(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctors_database')

    data = {'item': doctor, }

    return render(request, 'dm_doctors/doctor_delete.html',
                  data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def doctors_database(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_doctor_list = Doctor.objects.filter(
            Q(first_name__icontains=q) | Q(surname__icontains=q) | Q(middle_name__icontains=q) | Q(
            department__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q)
        ).order_by('-date_created')

    else:
        all_doctor_list = Doctor.objects.all().order_by('-date_created')
    paginator = Paginator(all_doctor_list, 15)
    page = request.GET.get('page')
    all_doctor = paginator.get_page(page)

    data = {
        'doctors': all_doctor,
    }
    return render(request,
                  'dm_doctors/doctors_database.html',
                  data)



# payment Create


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def payment_create(request):
    if request.method == 'POST':
        if request.POST.get('income') and request.POST.get('payment_method') and request.POST.get('technical_cost') and request.POST.get('evening_shift') and request.POST.get('patient') and request.POST.get('doctor') or request.POST.get('procedurs'):
            payment = Payment()
            payment.income = request.POST.get('income')
            payment.payment_method = request.POST.get('payment_method')
            payment.technical_cost = request.POST.get('technical_cost')
            payment.evening_shift = request.POST.get('evening_shift')
            payment.patient = request.POST.get('patients')
            payment.doctor = request.POST.get('doctors')
            payment.procedurs = request.POST.get('procedurs')
            payment.save()
            messages.success(request, 'Пациент успешно зарегистрирован!')
            return HttpResponseRedirect('payments_database')
    else:
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()
        procedurs = Procedur.objects.all()
        data = {
            'patients': patients,
            'doctors': doctors,
            'procedurs': procedurs,
        }
        return render(request,
                      'dm_payments/payment_create.html',
                      data)

# payment (need for Database)
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def payment(request, payment_id):
    payment = Payment.objects.get(id = payment_id)
    data = {
        'payment': payment,
    }
    if payment != None:
        return render(request, 'dm_payments/payment_update.html', data)

# payment update
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def payment_update(request):
    if request.method == 'POST':
        payment = Payment.objects.get(id= request.POST.get('id'))
        if payment != None:

            payment.first_name = request.POST.get('income')
            payment.surname = request.POST.get('payment_method')
            payment.middle_name = request.POST.get('technical_cost')
            payment.phone = request.POST.get('evening_shift')
            payment.iin = request.POST.get('patient')
            payment.gender = request.POST.get('doctor')
            payment.age = request.POST.get('procedurs')
            payment.save()

            messages.success(request, 'Данные о транзакции изменены!')
            return HttpResponseRedirect('payments_database')

# payment Delete
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def payment_delete(request, pk):
    payment = Payment.objects.get(id=pk)
    if request.method == "POST":
        payment.delete()
        return redirect('payments_database')

    data = {'item': payment, }

    return render(request, 'dm_payments/payment_delete.html',
                  data)

# payment Database
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def payments_database(request):

    if 'q' in request.GET:
        q = request.GET['q']
        all_payment_list = Payment.objects.filter(
            Q(income__icontains=q) | Q(payment_method__icontains=q) | Q(technical_cost__icontains=q) | Q(
                evening_shift__icontains=q) | Q(patient__icontains=q) | Q(doctor__icontains=q) | Q(procedurs__icontains=q)
        ).order_by('-date_created')

    else:
        all_payment_list = Payment.objects.all().order_by('-date_created')
    paginator = Paginator(all_payment_list, 15)
    page = request.GET.get('page')
    all_payment = paginator.get_page(page)

    data = {
        'payments': all_payment,
    }
    return render(request,
                  'dm_payments/payments_database.html',
                  data)




@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def procedur_create(request):
    submitted = False
    if request.method == 'POST':
        form = ProcedurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/procedur_create?submitted=True')
    else:
        form = ProcedurForm
        if 'submitted' in request.GET:
            submitted = True
    data = {
        'form': form,
        'submitted': submitted,
            }
    return render(request,
                'dm_procedurs/procedur_create.html',
                data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def procedur_personal_page(request, pk):
    procedurs = Procedur.objects.get(id=pk)

    payments = procedurs.payment_set.all()

    data = {
            'procedurs': procedurs,
            'payments': payments,
            }
    return render(request,
                  'dm_procedurs/procedur_personal_page.html',
                  data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def procedur_update(request, pk):
    procedur = procedur.objects.get(id=pk)
    form = ProcedurForm(instance=procedur)

    if request.method == 'POST':
        form = ProcedurForm(request.POST, instance=procedur)
        if form.is_valid():
            form.save()
            return redirect('procedurs_database')

    data = {'form': form, }
    return render(request,
                'dm_procedurs/procedur_create.html',
                data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def procedur_delete(request, pk):
    procedur = Procedur.objects.get(id=pk)
    if request.method == "POST":
        procedur.delete()
        return redirect('procedurs_database')

    data = {'item': procedur, }

    return render(request, 'dm_procedurs/procedur_delete.html',
                  data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def procedurs_database(request):
    procedurs = Procedur.objects.all()

    procedurfilter = ProcedurFilter(request.GET, queryset=procedurs)
    procedurs = procedurfilter.qs

    data = {
            'procedurfilter': procedurfilter,
            'procedurs': procedurs,
            }
    return render(request,
                  'dm_procedurs/procedurs_database.html',
                  data)
'''