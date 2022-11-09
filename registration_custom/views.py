from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, AccountAuthenticateForm, AccountUpdateForm

def index_view(request):
    return render(request, "accounts/indexbase.html", {})


def privacy_policy_view(request):
    return render(request, "accounts/PrivacyPolicy.html", {})


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save User data
            # login user with newly register data
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AccountAuthenticateForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect('index')
        else:
            context['login_form'] = form
    else:
        form = AccountAuthenticateForm()
        context['login_form'] = form
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required()
def account_view(request):
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            context['success_message'] = 'Data Updated'
    else:
        form = AccountUpdateForm(initial={
            'first_name': request.user.first_name,
            'middle_name': request.user.username,
            'surname': request.user.surname,
            'email': request.user.email,
            'dob': request.user.dob,
            'image': request.user.image.url,
            'username': request.user.username,
            'FIO': request.user.FIO
            }
        )
    context['account_form'] = form
    return render(request, 'accounts/profile.html', context)