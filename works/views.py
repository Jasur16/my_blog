from django.shortcuts import render
from .models import WorksModel
from django.views.generic import ListView, DetailView
from .models import WorksCategoryModel



class WorksView(ListView):
    model = WorksModel
    template_name = 'main/works.html'
    
class WorkDetailView(DetailView):
    model = WorksModel
    template_name = 'main/work_in.html'