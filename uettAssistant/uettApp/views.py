from django.shortcuts import render
from .models import *

# Create your views here.
# def home(request):
#     deps = Department.objects.all()
#     context = {'deps':deps}
#     return render(request,'uettApp/home.html',context)


def home(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'uettApp/home.html', context)


# def home(request):
#     # Retrieve all departments
#     departments = Department.objects.all()
    
#     # Create an empty dictionary to store departments and their associated semesters
#     department_semesters = {}

#     # Loop through each department
#     for department in departments:
#         # Retrieve all semesters related to the current department
#         semesters = department.semester_set.all()
#         # Store the department and its semesters in the dictionary
#         department_semesters[department] = semesters

#     # Pass the dictionary to the template context
#     context = {'department_semesters': department_semesters}
#     return render(request, 'uettApp/home.html', context)