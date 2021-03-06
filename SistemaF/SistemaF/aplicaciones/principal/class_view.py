from re import template
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.views.generic.base import View
from .forms import EmpleadoForms
from .models import Employees
from django.db.models import Q
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet 
from django import forms
 

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
    template_name = 'actualizarEmpleado.html'
    success_url = reverse_lazy('index')

class EmpleadoDelete(DeleteView):
    model = Employees
    template_name = 'verificacion.html'
    success_url=reverse_lazy('index')

class ReportePDF(View):
    def cabecera(self,pdf):
       #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = archivo_imagen = settings.MEDIA_ROOT+'/imagenes/descargar.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)  
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(235, 790, u"SISTEMA ITSJ ")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE EMPLEADOS")


    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('DNI', 'Nombre', 'Apellido Paterno', 'Apellido Materno')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(persona.emp_no, persona.first_name, persona.last_name, persona.gender) for persona in Employees.objects.first()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)
    
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
