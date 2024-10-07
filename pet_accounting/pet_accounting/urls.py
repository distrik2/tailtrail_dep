# pet_accounting/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from pets import views as pet_views
from django.conf import settings
from django.conf.urls.static import static
from pets import views
from django.urls import path, include
from rest_framework import routers
from pets.views import my_api_view


# router = routers.DefaultRouter()
# router.register(r'api/pets', views.PetProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', pet_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='pets/login.html'), name='login'),
    path('logout/', pet_views.logout_view, name='logout'),
    # path('profile/', pet_views.profile, name='profile'),  # URL для страницы профиля
    path('', pet_views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('pick_up_pet/<int:booking_id>/', views.pick_up_pet, name='pick_up_pet'),
    path('api/message/', my_api_view, name='api_message'),
    # path('api/example/', views.example_api_view, name='example_api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
