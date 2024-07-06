from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path("", views.getRoutes, name="routes"),
    path("departments/", views.theDepartments, name="departments"),
    path("departments/<str:pk>/", views.departmentDetails, name="department"),
    path("subjects/", views.getSubjects, name="subjects"),
    path("subjects/<str:pk>/", views.getSubject, name="subject"),
    path("semesters/", views.getSemesters, name="semesters"),
    path("semesters/<str:pk>/", views.getSemester, name="semester"),
    path("titlepage/", views.setTitlePage, name="titlePage"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
