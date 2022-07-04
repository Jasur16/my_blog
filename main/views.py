from django import views
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View



class HomeView(TemplateView):
    template_name = 'main/home.html'

class ContactView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main/contact.html')

    def post(self, request, *args, **kwargs):
        return redirect('contact')