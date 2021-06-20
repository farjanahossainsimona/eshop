from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.db.models import Q
from .models import User


class IndexView(generic.View):
    template_name = 'account/index.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(generic.View):
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(Q(email=email), Q(password=password))
        if user:
            request.session['logged_user'] = user[0].id
            return redirect('account.index')
        else:
            messages.error(request, 'Login Failed')
            return redirect('login')

class RegisterView(generic.View):
    template_name = 'account/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = first_name + last_name
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if(password == confirm_password):
            # insert/create query
            user = User(username=username,
                    first_name=first_name, last_name=last_name, email=email, phone=phone, password=password)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('register')
        else:
            messages.info(request, 'Password not matching..')
            return redirect('register')