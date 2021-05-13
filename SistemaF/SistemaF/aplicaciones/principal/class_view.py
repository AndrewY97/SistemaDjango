from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .forms import EmpleadoForms
from .models import Employees

class EmpleadoList(ListView):
    model = Employees
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()[10:]