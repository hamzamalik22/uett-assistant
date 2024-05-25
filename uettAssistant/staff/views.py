from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
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
            messages.error(request, 'Usernamee or password incorrect.')

    context = {'title': 'Staff Login'}
    return render(request, 'staff/login_page.html', context)


@login_required(login_url='staff_login')
def staff_panel(request):
    context = {'title': 'Dashboard'}
    return render(request, 'staff/Dashboard.html', context)
