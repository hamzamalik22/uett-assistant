from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('calculator/<str:department_id>/<str:semester_id>/', views.calculator, name='calculator'),
]
