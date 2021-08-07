from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    # ****************** Authentications ***********************


    path('login/', views.loginPage.as_view(), name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('changepassword/', views.changePassword.as_view(), name="changepassword"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="dashboard/reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="dashboard/reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="dashboard/reset_password_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="dashboard/reset_password_complete.html"),
         name="password_reset_complete"),
         
    # *************************************************


    # ****************** Dashboard ***********************

    path('dashboard/', views.Dashboard, name='dashboard'),



    # ****************** Website ***********************

    path('', views.Home, name='home'),

    # *************************************************

    # ------------------About & Courses------------------
    path('courses/', views.courses, name='courses'),
    path('courses_details/', views.courses_details, name='courses_details'),
    path('about/', views.about, name='about')

]
