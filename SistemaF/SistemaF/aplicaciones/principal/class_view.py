from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .forms import EmpleadoForms
from .models import Employees

class EmpleadoList(ListView):
    model = Employees
    template_name = 'index.html'

class EmpleadoCrear(CreateView):
    model = Employees
    form_class = EmpleadoForms
    template_name = 'crearEmpleado.html'
    success_url = reverse_lazy('index')

class EmpleadoUpdate(UpdateView):
    model = Employees
    form_class = EmpleadoForms
    template_name = 'crearEmpleado.html'
    success_url = reverse_lazy('index')

class EmpleadoDelete(DeleteView):
    model = Employees
    template_name = 'verificacion.html'
    success_url=reverse_lazy('index')
