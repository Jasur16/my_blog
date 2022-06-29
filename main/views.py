from django.shortcuts import render
from django.views.generic import TemplateView, CreateView



class HomeView(TemplateView):
    template_name = 'main/home.html'

class ContactView(CreateView):
    template_name = 'main/contact.html'