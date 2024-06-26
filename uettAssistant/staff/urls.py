from django.urls import path
from . import views

urlpatterns = [
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staff_panel/', views.staff_panel, name='staff_panel'),
    path('logoutPage/', views.logoutUser, name='logout'),

    path('department/create/', views.depCreate, name='dep_create'),
    path('depUpdate/<str:pk>/',views.depUpdate,name='depUpdate'),
    path('depDelete/<str:pk>/',views.depDelete,name='depDelete'),

    path('semester/create/', views.semCreate, name='sem_create'),
    path('semUpdate/<str:pk>/',views.semUpdate,name='semUpdate'),
    path('semDelete/<str:pk>/',views.semDelete,name='semDelete'),

    path('subject/create/', views.subCreate, name='sub_create'),
    path('subUpdate/<str:pk>/',views.subUpdate,name='subUpdate'),
    path('subDelete/<str:pk>/',views.subDelete,name='subDelete'),
]
