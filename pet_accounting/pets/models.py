# pets/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Employee(models.Model):
    # Модель сотрудника (остается без изменений)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    rating = models.PositiveIntegerField(default=0, choices=[(i, f'{i} Stars') for i in range(1, 6)])
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.rating} Stars)'


class PetProfile(models.Model):
    # Модель питомца (как раньше)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    pet_name = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100)
    pet_age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.full_name} - {self.pet_name}'



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.PositiveIntegerField()  # Длительность в часах
    # duration = models.IntegerField(default=1)  
    created_at = models.DateTimeField(auto_now_add=True)
    picked_up = models.BooleanField(default=False)  # Был ли питомец забран

    def __str__(self):
        return f'Бронирование от {self.user.username} для {self.pet.pet_name}'

