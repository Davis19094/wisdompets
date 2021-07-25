
from django.contrib import admin
from django.urls import path

from adoption import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('adoption/<int:pet_id>', views.pet_detail, name = 'pet_detail'),
]
