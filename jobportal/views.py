from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, HttpResponse
from .forms import MyUserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from employee.models import Employee

from django.contrib.auth import logout


def signin(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            if not isEmployer(request.user.id) and not isEmployee(request.user.id):
                return redirect('who')
            if isEmployee(request.user.id):
                return redirect('empdashboard')
        else:
            messages.add_message(request, messages.SUCCESS, " username or password does not valid")
    return render(request, 'login.html', {'form': form})


def signup(request):
    form = MyUserCreationForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.add_message(request, messages.SUCCESS, "account created sucessfully")
            return redirect('signin')
        except ValidationError as e:
            messages.add_message(request, messages.ERROR, e.messages)
    return render(request, 'signup.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def who(request):
    return render(request, 'who.html')


@login_required(login_url='signin')
def dashboard(request):
    a = isEmployee(request.user.id)
    return HttpResponse(f"<h1>Dashboard" + str(a) + " </h1>")


def isEmployee(user_id):
    try:
        e = Employee.objects.get(user_id=user_id)
        return True
    except:
        return False


def isEmployer(user_id):
    try:
        e = Employer.objects.get(user_id=user_id)
        return True
    except:
        return False
