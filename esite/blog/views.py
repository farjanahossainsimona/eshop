from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Blog


class IndexView(generic.View):
    template_name = 'blog/index.html'

    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, self.template_name, {'blogs': blogs})
