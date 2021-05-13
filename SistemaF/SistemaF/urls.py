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
from SistemaF.aplicaciones.principal.views import inicio,crearPersona,editarEmpleado,eliminarEmpleado
from SistemaF.aplicaciones.principal.class_view import EmpleadoList

#from SistemaF.views import despedida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',EmpleadoList.as_view(),name='index'),
    path('crearEmpleado/',crearPersona,name='crearEmpleado'),
    path('editarEmpleado/<int:emp_no>/',editarEmpleado,name='editarEmpleado'),
    path('eliminarEmpleado/<int:emp_no>',eliminarEmpleado,name='eliminarEmpleado'),
]
