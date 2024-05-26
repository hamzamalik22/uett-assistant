from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from uettApp.models import *
from .forms import *
# Create your views here.

def staff_login(request):
    if request.user.is_authenticated:
        return redirect('staff_panel')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User doesn't exist.")
            return redirect('staff_login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('staff_panel')
        else:
            messages.error(request, 'Incorrect Password 😐')

    context = {'title': 'Staff Login'}
    return render(request, 'staff/login_page.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('staff_login')


@login_required(login_url='staff_login')
def staff_panel(request):
    departments = Department.objects.all()
    subjects = Subject.objects.all()
    semesters = Semester.objects.all()


    context = {'title': 'Dashboard','departments': departments, 'subjects' : subjects, 'semesters' : semesters}
    return render(request, 'staff/Dashboard.html', context)


# Department update & Delete 

@login_required(login_url='staff_login')
def depUpdate(request, pk):
    dep = get_object_or_404(Department, id=pk)
    form = DepForm(instance=dep)
    
    if request.method == 'POST':
        form = DepForm(request.POST, instance=dep)
        if form.is_valid():
            form.save()
            return redirect('staff_panel')
    
    context = {'form': form}
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'staff/update.html', context)
    else:
        return render(request, 'staff/update.html', context)

@login_required(login_url='staff_login')
def depDelete(request,pk):
    dep = Department.objects.get(id=pk)

    if request.method == 'POST':
        dep.delete()
        return redirect("staff_panel")
    
    context = {'item' : dep}

    return render(request,"staff/delete.html",context)

# Semester update & Delete 

@login_required(login_url='staff_login')
def semUpdate(request,pk):
    sem = Semester.objects.get(id=pk)

    form = SemForm(instance=sem)

    if request.method == 'POST':
        form = SemForm(request.POST,instance=sem)
        if form.is_valid():
            form.save()
        return redirect('staff_panel')

    context = {'form' : form}

    return render(request,'staff/update.html',context)

@login_required(login_url='staff_login')
def semDelete(request,pk):
    sem = Semester.objects.get(id=pk)

    if request.method == 'POST':
        sem.delete()
        return redirect("staff_panel")
    
    context = {'item' : sem}

    return render(request,"staff/delete.html",context)


# Subject Update & Delete


@login_required(login_url='staff_login')
def subUpdate(request,pk):
    sub = Subject.objects.get(id=pk)

    form = SubForm(instance=sub)

    if request.method == 'POST':
        form = SubForm(request.POST,instance=sub)
        if form.is_valid():
            form.save()
        return redirect('staff_panel')

    context = {'form' : form}

    return render(request,'staff/update.html',context)

@login_required(login_url='staff_login')
def subDelete(request,pk):
    sub = Subject.objects.get(id=pk)

    if request.method == 'POST':
        sub.delete()
        return redirect("staff_panel")
    
    context = {'item' : sub}

    return render(request,"staff/delete.html",context)
