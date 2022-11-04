from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='tracker/login.html')),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tracker/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:laptop_pk>/issue/add', views.IssueCreate.as_view(), name='add-issue'),
    path('profile/<int:laptop_pk>/issue/<int:pk>/update', views.IssueUpdate.as_view(), name='update-issue'),
    #path('profile/<int:laptop_pk>/issue/<int:pk>/delete', views.IssueDeleteView.as_view(), name='issue-delete'),

]

