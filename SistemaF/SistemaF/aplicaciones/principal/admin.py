from django.contrib import admin

from .models import Employees
from .models import Departments

admin.site.register(Employees)
admin.site.register(Departments)


# Register your models here.
