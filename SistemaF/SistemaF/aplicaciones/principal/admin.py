from django.contrib import admin

from .models import Employees,Salaries,Departments,Titles

admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(Salaries)
admin.site.register(Titles)


# Register your models here.
