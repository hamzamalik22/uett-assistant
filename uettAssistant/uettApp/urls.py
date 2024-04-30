from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gpa/', views.gpa, name='gpa'),
    path('calculator/<str:department_id>/<str:semester_id>/', views.calculator, name='calculator'),
]
