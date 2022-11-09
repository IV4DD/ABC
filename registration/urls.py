from django.urls import path, include
from . import views

urlpatterns = [

    # Login
    path('login/', views.login, name='login'),

    # Logout
    path('', include('django.contrib.auth.urls')),

    # Primary Registration
    path('primary_registration', views.primary_registration, name='primary_registration'),

    # Pending Account
    path('pending', views.pending, name='pending'),

    # Registration
    path('register', views.register, name='register'),

    # Welcome Page
    path('', views.welcome, name='welcome'),

    # Backend HR Approvers Page
    path('backend', views.backend, name='backend'),

    # Backend Account Personal Page
    path('account_personal_page/<str:username>/', views.account_personal_page, name='account_personal_page'),

]
