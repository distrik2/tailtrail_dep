# pets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from .models import PetProfile
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import PetProfile, Employee, Booking
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from datetime import timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            PetProfile.objects.create(
                user=user,
                telegram_id=form.cleaned_data.get('telegram_id'),
                full_name=form.cleaned_data.get('full_name'),
                phone_number=form.cleaned_data.get('phone_number'),
                pet_name=form.cleaned_data.get('pet_name'),
                pet_breed=form.cleaned_data.get('pet_breed'),
                pet_age=form.cleaned_data.get('pet_age')
            )
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'pets/register.html', {'form': form})

def home(request):
    # Если пользователь авторизован, перенаправляем его на страницу профиля
    if request.user.is_authenticated:
        return redirect('profile')
    
    return render(request, 'pets/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')

# pets/views.py
@login_required
def profile(request):
    pet_profile = PetProfile.objects.get(user=request.user)
    employees = Employee.objects.all()
    bookings = Booking.objects.filter(user=request.user, picked_up=False)

    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = Employee.objects.get(id=employee_id)
        hours = int(request.POST.get('hours'))  # Количество часов

        start_time = timezone.now()
        end_time = start_time + timedelta(hours=hours)

        Booking.objects.create(
            user=request.user, 
            pet=pet_profile, 
            employee=employee, 
            start_time=start_time, 
            end_time=end_time, 
            duration=hours
        )

        return redirect('profile')

    return render(request, 'pets/profile.html', {
        'pet_profile': pet_profile,
        'employees': employees,
        'bookings': bookings
    })

@login_required
def pick_up_pet(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.picked_up = True
    booking.save()
    return redirect('profile')




@api_view(['GET'])
def my_api_view(request):
    data = {"message": "Hello from Django"}
    return Response(data)

