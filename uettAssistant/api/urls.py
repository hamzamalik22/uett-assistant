from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("departments/", views.getDepartments, name="departments"),
    path("departments/<str:pk>/", views.getDepartment, name="department"),
    path("subjects/", views.getSubjects, name="subjects"),
    path("subjects/<str:pk>/", views.getSubject, name="subject"),
    path("semesters/", views.getSemesters, name="semesters"),
    path("semesters/<str:pk>/", views.getSemester, name="semester"),
    path("titlepage/", views.setTitlePage, name="titlePage"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
