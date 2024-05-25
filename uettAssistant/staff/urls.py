from django.urls import path
from . import views

urlpatterns = [
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staff_panel/', views.staff_panel, name='staff_panel'),
]
