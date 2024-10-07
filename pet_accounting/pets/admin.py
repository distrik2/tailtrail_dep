# pets/admin.py
from django.contrib import admin
from .models import PetProfile, Employee

admin.site.register(PetProfile)
admin.site.register(Employee)  # Регистрация модели сотрудника
