from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .forms import EmpleadoForms
from .models import Employees

class EmpleadoList(ListView):
    template_name='index.html'
    queryset= Employees.objects.all().order_by('emp_no')
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']='Listado de Empleados'

        return context

    

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
