from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

def LoginView(request):

    context = {

    }
    return render(request, 'account/login.html', context)

def LogoutView(request):

    return 
