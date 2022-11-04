from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Employee, Department, offices, Issue, Laptop


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(label='Username')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(),
            'password1': forms.PasswordInput(attrs={'autocomplete': 'on'}),
            'password2': forms.PasswordInput(attrs={'autocomplete': 'on'}),
        }
        # help_texts = {k: "" for k in fields}
        labels = {k: "" for k in fields}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class EmployeeUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = ['department', 'office']
        widgets = {
            'department': forms.Select(attrs={'placeholder': 'Department'}),
            'office': forms.Select(attrs={'placeholder': 'Office', 'choices': offices})
        }


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the problem.'})
        }

