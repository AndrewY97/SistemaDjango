from threading import ExceptHookArgs
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .models import Employees
from .forms import EmpleadoForms

def inicio(request):
    personas = Employees.objects.all()
    contexto={
        'personas':personas
    }      
    return render(request,'index.html',contexto)

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