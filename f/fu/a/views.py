from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Coc


class Mailgb(TemplateView):
    template_name = "det.html"

class UserList(ListView):
    model = Coc
    context_object_name = "users"
    template_name = 'index.html'

class UserDetail(DetailView):
     model = Coc
     context_object_name = "sers"
     template_name = "index2.html"