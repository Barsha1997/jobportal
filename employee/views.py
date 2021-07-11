from django.shortcuts import render, redirect
from .form import EmployeeCreateForm, AddSkillForm, ChangeProfileImageForm, AboutEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee, Skill


def create(request):
    form = EmployeeCreateForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.save()
        messages.add_message(request, messages.SUCCESS, "sucessfully created")
        return redirect('empdashboard')
    return render(request, 'employee/create.html', {'form': form})


@login_required(login_url='signin')
def dashboard(request):
    e = getCurrentlyloginEmployee(request.user)
    skillForm = AddSkillForm(request.POST or None)
    changeImageForm = ChangeProfileImageForm(request.POST or None, request.FILES or None, instance=e)
    aboutMeForm = AboutEditForm(request.POST or None, instance=e)
    if aboutMeForm.is_valid():
        aboutMeForm.save()
        messages.add_message(request, messages.SUCCESS, "Sucessfully changed")

    if changeImageForm.is_valid():
        changeImageForm.save()
        messages.add_message(request, messages.SUCCESS, "Sucessfully changed")
    context = {}
    context.update({'changeImageForm': changeImageForm,'aboutform':aboutMeForm})
    if skillForm.is_valid():
        data = skillForm.save(commit=False)
        data.employee = e
        data.save()
        messages.add_message(request, messages.SUCCESS, "successfully saved")
        skillForm = AddSkillForm()
    context.update({'skillform': skillForm})
    skills = Skill.objects.filter(employee=e)
    context.update({'skills': skills})
    if e == None:
        pass
    else:
        context.update({'employee': e})
    return render(request, 'employee/dashboard.html', context)


def getCurrentlyloginEmployee(user):
    try:
        return Employee.objects.get(user)
    except:
        return None
