from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, EmployeeUpdateForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee


# TODO:
#  +allow users to request laptops
#  +track laptop issues (including action required and where it went for repairs if necessary)
#  +Suppliers list (Name, address, number, email, contact person)
#  +managers view for their departments
#  + try this for the form styling https://cdn.jsdelivr.net/npm/@codolog/form@1.0.0/dist/form.css,
#  ref: https://github.com/the94air/form

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'tracker/register.html', {'form': form})


def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        form = EmployeeUpdateForm(request.POST, instance=request.user.employee)
        if form.is_valid() and u_form.is_valid():
            u_form.save()
            form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        form = EmployeeUpdateForm(instance=request.user.employee)
        u_form = UserUpdateForm(instance=request.user)

    if hasattr(request.user.employee, 'laptop'):  # check if employee has laptop with hasattr; try-except would work too
        laptop = request.user.employee.laptop
    else:
        laptop = False

    context = {
        'form': form,
        'u_form': u_form,
        'laptop':  laptop
    }
    return render(request, 'tracker/profile.html', context)
