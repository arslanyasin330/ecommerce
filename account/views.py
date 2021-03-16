from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect

from account.forms import LoginForm, UserEditForm
from .forms import UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # authenticate  check user exist or not
            user = authenticate(request,
                                username=cd['email'],
                                phone_number=cd['phone_number'],
                                password=cd['password'])

            if user:
                # login  save user in session
                login(request, user)
                return render(request, 'shop/dashboard.html')
                # return HttpResponse('Authenticated successfully')

            else:
                messages.error(request, 'User name ,  password is not correct')
                return redirect('login')

        else:
            return render(request, 'account/login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    auth.logout(request)
    return render(request, 'shop/dashboard.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            messages.success(request, f'Welcome {new_user.first_name}!Your account has been successfully created. Now '
                                      f'you can login')
            return redirect('login')
        else:
            return render(request,
                          'account/register.html',
                          {'user_form': user_form})

    else:
        user_form = UserRegistrationForm()
        return render(request,
                      'account/register.html',
                      {'user_form': user_form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(instance=request.user,
                                      data=request.POST)
        if user_edit_form.is_valid():

            user_edit_form.save()

            messages.success(request, 'profile edited successfully')
            return redirect('/')
        else:
            return render(request,
                          'account/edit_profile.html',
                          {'user_form': user_edit_form})

    else:
        user_form = UserEditForm(instance=request.user)
        return render(request,
                      'account/edit_profile.html',
                      {'user_form': user_form})
