from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import GradeForm

def gpa(request):
    departments = Department.objects.all()
    semesters = Semester.objects.all()  # Get all semesters
    context = {'departments': departments, 'semesters': semesters}
    return render(request, 'uettApp/gpa.html', context)


def home(request):
    departments = Department.objects.all()
    semesters = Semester.objects.all()  # Get all semesters
    context = {'departments': departments, 'semesters': semesters}
    return render(request, 'uettApp/home.html', context)


# def calculator(request, department_id, semester_id):
#     department = get_object_or_404(Department, id=department_id)
#     semester = get_object_or_404(Semester, id=semester_id, department=department)
#     subjects = semester.subjects.all()

#     if request.method == 'POST':
#         grade_form = GradeForm(request.POST, subjects=subjects)
#         if grade_form.is_valid():
#             total_grade_points = 0
#             total_credit_hours = 0

#             for subject in subjects:
#                 grade = grade_form.cleaned_data.get(f'grade_{subject.id}')
#                 credit_hours = subject.credit_hour
#                 print(f"Subject: {subject.name}, Grade: {grade}, Credit Hours: {credit_hours}")

#                 if grade == 'A':
#                     grade_points = 4.0
#                 elif grade == 'A-':
#                     grade_points = 3.7
#                 elif grade == 'B+':
#                     grade_points = 3.3
#                 elif grade == 'B':
#                     grade_points = 3.0
#                 elif grade == 'B-':
#                     grade_points = 2.7
#                 elif grade == 'C+':
#                     grade_points = 2.3
#                 elif grade == 'C':
#                     grade_points = 2.0
#                 elif grade == 'C-':
#                     grade_points = 1.7
#                 elif grade == 'D':
#                     grade_points = 1.0
#                 else:
#                     grade_points = 0.0  

#                 total_grade_points += grade_points * credit_hours
#                 total_credit_hours += credit_hours

#             if total_credit_hours != 0:
#                 gpa = total_grade_points / total_credit_hours
#                 gpa = "{:.3f}".format(gpa)
#                 gpa = gpa[:4]
#             else:
#                 gpa = None 

#             context = {'department': department, 'semester': semester, 'subjects': subjects, 'grade_form': grade_form, 'gpa': gpa}
#             return render(request, 'uettApp/calculator.html', context)
#     else:
#         grade_form = GradeForm(subjects=subjects)

#     context = {'department': department, 'semester': semester, 'subjects': subjects, 'grade_form': grade_form}
#     return render(request, 'uettApp/calculator.html', context)



def calculator(request, department_id, semester_id):
    department = get_object_or_404(Department, id=department_id)
    semester = get_object_or_404(Semester, id=semester_id, department=department)
    subjects = semester.subjects.all()

    if request.method == 'POST':
        grade_form = GradeForm(request.POST, subjects=subjects)
        if grade_form.is_valid():
            subject_gpas = {}
            total_grade_points = 0
            total_credit_hours = 0

            for subject in subjects:
                grade = grade_form.cleaned_data.get(f'grade_{subject.id}')
                credit_hours = subject.credit_hour

                if grade == 'A':
                    grade_points = 4.0
                elif grade == 'A-':
                    grade_points = 3.7
                elif grade == 'B+':
                    grade_points = 3.3
                elif grade == 'B':
                    grade_points = 3.0
                elif grade == 'B-':
                    grade_points = 2.7
                elif grade == 'C+':
                    grade_points = 2.3
                elif grade == 'C':
                    grade_points = 2.0
                elif grade == 'C-':
                    grade_points = 1.7
                elif grade == 'D':
                    grade_points = 1.0
                else:
                    grade_points = 0.0  

                gpa = grade_points * credit_hours
                subject_gpas[subject.name] = gpa

                total_grade_points += gpa
                total_credit_hours += credit_hours

            total_gpa = total_grade_points / total_credit_hours
            total_gpa = round(total_gpa, 2)

            context = {'department': department, 'semester': semester, 'subjects': [subject.name for subject in subjects], 'subject_gpas': list(subject_gpas.values()), 'total_gpa': total_gpa}
            return render(request, 'uettApp/calculator.html', context)
    else:
        grade_form = GradeForm(subjects=subjects)

    context = {'department': department, 'semester': semester, 'subjects': subjects, 'grade_form': grade_form}
    return render(request, 'uettApp/calculator.html', context)