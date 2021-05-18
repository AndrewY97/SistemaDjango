from re import template
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .forms import EmpleadoForms
from .models import Employees
from django.db.models import Q

class EmpleadoList(ListView):
    template_name='index.html'
    queryset= Employees.objects.all().order_by('emp_no')
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']='Listado de Empleados'
        return context
    #Empleado=Employees.objects.filter()

def buscar(request):
    print(request.GET)
    #queryset= request.GET.get("buscar")
    empleados=Employees.objects.filter(emp_no=True)
    return render(request,'index.html',{'empleados':empleados})
    

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


