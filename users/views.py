from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == 'GET':
        context_data = {
            'form':RegisterForm
        }

        return render(request, 'users/register.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data.get('password1') == cleaned_data.get('password2'):
                User.objects.create_user(
                    username=cleaned_data.get('username'),
                    password=cleaned_data.get('password1'),

                )
                return redirect('/users/login/')
            else:
                form.add_error('password2', 'try again')
        context_data = {
            'form':form
        }

        return render(request, 'users/register.html', context=context_data)

def login_view(request):
    if request.method == 'GET':
        context_data = {
            'form':LoginForm
        }

        return render(request, 'users/login.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data=data)

        if form.is_valid():
            """authenticate"""
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )

            if user:
                """authorization"""
                login(request=request, user=user)
                return redirect('/posts/')
            else:
                form.add_error('username', 'try again')

        context_data = {
            'form':form
        }
        return render(request, 'users/login.html', context=context_data)


def logout_view(request):
    logout(request)
    return redirect('/posts/')