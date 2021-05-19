"""SistemaF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from SistemaF.aplicaciones.principal.views import inicio,crearPersona,editarEmpleado,eliminarEmpleado,categoria_print
from SistemaF.aplicaciones.principal.class_view import EmpleadoList,EmpleadoCrear,EmpleadoUpdate,EmpleadoDelete,ReportePDF
from SistemaF.aplicaciones.usuarios.views import Login, salir

#from SistemaF.views import despedida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login.as_view(),name='login'),
    path('principal/', login_required(EmpleadoList.as_view()),name='index'),
    path('principall/', login_required(inicio),name='index2'),
    path('crearEmpleado/',login_required(EmpleadoCrear.as_view()),name='crearEmpleado'),
    path('editarEmpleado/<int:pk>/',login_required(EmpleadoUpdate.as_view()),name='editarEmpleado'),
    path('eliminarEmpleado/<int:pk>',login_required(EmpleadoDelete.as_view()),name='eliminarEmpleado'),
    path('logout/',login_required(salir),name='logout'),
     path('categorias/print/<int:pk>', categoria_print, name='categoria_print_one'),  
    #path('busqueda/',buscar,name='busqueda')
]
