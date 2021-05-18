from threading import ExceptHookArgs
from django.core import paginator
from django.db.models import query
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .models import Employees
from .forms import EmpleadoForms
from django.core.paginator import Paginator
from django.db.models import Q

def inicio(request):
    #print(request.GET)
    queryset= request.GET.get("buscar")
    print(queryset)
    empleados=Employees.objects.filter(emp_no=True)
    if queryset:
        empleados= Employees.objects.filter(
            Q(emp_no__iexact=queryset)|
            Q(first_name__icontains=queryset)|
            Q(last_name__icontains=queryset)
        ).distinct()
    return render(request,'index2.html',{'empleados':empleados})

def crearPersona(request):
    if request.method=='GET':
        form = EmpleadoForms()
        contexto={
            'form':form
        }
    else:
        form = EmpleadoForms(request.POST)
        print(form)
        contexto={
            'form':form
        } 
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearEmpleado.html',contexto)

def editarEmpleado(request,emp_no):
    empleado = Employees.objects.get(emp_no = emp_no)
    if request.method=='GET':
        form = EmpleadoForms(instance=empleado)
        contexto={
            'form':form
        }
    else:
        form= EmpleadoForms(request.POST, instance=empleado)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save
            return redirect('index')
    return render(request,'crearEmpleado.html',contexto)

def eliminarEmpleado(request,emp_no):
    empleado = Employees.objects.get(emp_no=emp_no)
    empleado.delete()
    return redirect('index')
