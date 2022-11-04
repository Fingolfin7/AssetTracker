from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, EmployeeUpdateForm, UserUpdateForm, IssueForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Issue, Laptop, condition_levels


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

    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'tracker/register.html', context)


@login_required
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

    issues_list = False

    if hasattr(request.user.employee, 'laptop'):  # check if employee has laptop with hasattr; try-except would work too
        laptop = request.user.employee.laptop
        if hasattr(laptop, 'issue_set'):
            issues_list = laptop.issue_set.order_by("resolution_date")
    else:
        laptop = False

    context = {
        'form': form,
        'title': 'Dashboard',
        'u_form': u_form,
        'laptop':  laptop,
        'issues_list': issues_list,
    }
    return render(request, 'tracker/profile.html', context)


class IssueCreate(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'tracker/issue.html'
    success_url = 'profile'

    def form_valid(self, form):
        form.instance.laptop = Laptop.objects.get(id=self.kwargs['laptop_pk'])

        if form.is_valid():
            messages.success(self.request, "Issue Created Successfully.")
            form.instance.laptop.condition = condition_levels[1][0]
            form.instance.laptop.save()
            form.save()
            return self.get_success_url()

        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Issue'
        return context


class IssueUpdate(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'tracker/issue.html'
    success_url = 'profile'

    def form_valid(self, form):
        form.instance.laptop = Laptop.objects.get(id=self.kwargs['laptop_pk'])

        if form.is_valid():
            messages.success(self.request, "Issue Updated Successfully.")
            form.save()
            return self.get_success_url()

        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Issue'
        return context
