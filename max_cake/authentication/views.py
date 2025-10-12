from django.shortcuts import render, redirect

from django.views import View

from .forms import LoginForm, RegisterForm

from django.contrib.auth import authenticate, login, logout

from .utility import password_generator, sending_email

from django.contrib.auth.hashers import make_password

import threading

class LoginView(View):

    form_class = LoginForm

    def get(self, request, *args, **kwargs):

        form = self.form_class()

        data = {
            'form': form
        }

        return render(request, 'authentication/login.html', context=data)
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = authenticate(**form.cleaned_data)

            if user:

                login(request, user)

                return redirect('home')
            
            msg = 'Invalid Credentials'

        data = {
            'form': form,
            'msg': msg if 'msg' in locals() else None,
        }

        return render(request, 'authentication/login.html', context=data)
    
class LogoutView(View):

    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect('home')
    
class RegisterView(View):

    form_class = RegisterForm

    def get(self, request, *args, **kwargs):

        form = self.form_class()

        data = {
            'form': form
        }

        return render(request, 'authentication/register.html', context=data)
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        print(form.is_valid())

        if form.is_valid():

            user = form.save(commit=False)

            user.username = user.email

            user.email = 'User'

            password = password_generator()

            user.password = make_password(password)

            user.save()

            # Email Integration

            subject = 'Login Credentials'

            template = 'email/login_credentials.html'

            context = {
                'user': user,
                'password': password,
            }

            recipient = user.email

            print(recipient)

            thread = threading.Thread(target=sending_email, args=(subject, template, context, recipient))

            thread.start()

            # sending_email(subject, template, context, recipient)

            print('every')

            return redirect('login')
        
        data = {
            'form': form
        }
        
        return render(request, 'authentication/register.html', context=data)