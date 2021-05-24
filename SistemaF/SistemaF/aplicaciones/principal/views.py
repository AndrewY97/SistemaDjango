from threading import ExceptHookArgs
from django.shortcuts import redirect, render, HttpResponse
from .models import Employees
from .forms import EmpleadoForms
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
            Q(last_name__icontains=queryset)|
            Q(gender__icontains=queryset)|
            Q(hire_date__icontains=queryset)
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
        contexto['form'] = form
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

def categoria_print(self, pk=None):  
    import io  
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  
    from reportlab.lib.styles import getSampleStyleSheet  
    from reportlab.lib import colors  
    from reportlab.lib.pagesizes import letter  
    from reportlab.platypus import Table  

    response = HttpResponse(content_type='application/pdf')  
    buff = io.BytesIO()  
    doc = SimpleDocTemplate(buff,  
                pagesize=letter,  
                rightMargin=40,  
                leftMargin=40,  
                topMargin=60,  
                bottomMargin=18,  
                )  
    categorias = []  
    styles = getSampleStyleSheet()  
    header = Paragraph("Lista de Empleados", styles['Heading1'])  
    categorias.append(header)  
    headings = ('Emp. No', 'First Name', 'Last Name', 'Gender','Hire Date')  
    if not pk:  
        todascategorias = [(p.id, p.descripcion, p.activo, p.creado,p.otro)  
                for p in Employees.objects.all().order_by('pk')]  
    else: 
        todascategorias = [(p.emp_no, p.first_name, p.last_name, p.gender,p.hire_date)  
                for p in Employees.objects.filter(emp_no=pk)]   
    t = Table([headings] + todascategorias)  
    t.setStyle(TableStyle(  
        [  
        ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),  
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),  
        ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)  
        ]  
    ))  

    categorias.append(t)  
    doc.build(categorias)  
    response.write(buff.getvalue())  
    buff.close()  
    return response  