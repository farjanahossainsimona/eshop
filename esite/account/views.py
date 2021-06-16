from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class IndexView(generic.View):
    template_name = 'account/index.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(generic.View):
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name)