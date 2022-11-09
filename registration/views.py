from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from SD.forms import CoworkerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import AccountCreationForm, AccountAuthenticateForm
from .models import Account


# Welcome
def welcome(request):
    return render(request,
                  'registration/welcome.html',
                  )

# Login
def login(request):
    form = AccountAuthenticateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect('/SD/')
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AccountAuthenticateForm()
    return render(request,
                  'registration/login.html',
                  {'form': form},
                  )

# Logout
def logout(request):
    return render(request,
                  'registration/logout.html',
                  )




# Primary Registration
def primary_registration(request):
    form = AccountCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка на регистрацию отправлена на рассмотрение.'
                                      'После рассмотрения Вам будет выслано письмо с подтверждением.')
            return HttpResponseRedirect('/primary_registration')
        else:
            return render(request, 'registration/primary_registration.html', {'form': form})
    else:
        form = AccountCreationForm()
    return render(request, 'registration/primary_registration.html', {'form': form})


# Coworker Registration
def register(request):
    form = CoworkerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены!')
            return HttpResponseRedirect('/register')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CoworkerForm()
    return render(request, 'registration/register.html', {'form': form})


def backend(request):
    context = {'accounts': Account.objects.filter(status='На рассмотрении')}
    return render(request,
                  'registration/backend.html',
                  context)

# Access coworkers personal pages
def account_personal_page(request, username):
    account = Account.objects.get(pk=username)
    form = AccountCreationForm(request.POST, instance=account)
    if request.method == 'POST':
        array = [
            'first_name',
            'middle_name',
            'surname',
            'email',
            'username',
            'dob',
        ]
        for field in array:
            form.fields[field].disabled = True
        context = {'form': form,
                   'account': account}
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены!')
            return HttpResponseRedirect('/backend')
        else:
            return render(request, 'registration/backend.html', context)
    else:
        data = Account.objects.get(pk=username)
        form = AccountCreationForm(instance=data)
        account = Account.objects.get(pk=username)
        array = [
            'first_name',
            'middle_name',
            'surname',
            'email',
            'username',
            'dob',
        ]
        for field in array:
            form.fields[field].disabled = True
        context = {'form': form,
                   'account': account}
        return render(request, 'registration/account_personal_page.html', context)

# Pending Account
def pending(request):
    return render(request,
                  'registration/pending.html',
                  )