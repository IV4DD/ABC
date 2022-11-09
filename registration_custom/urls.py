from django.urls import path, include
from .views import registration_view, logout_view, login_view, account_view, index_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Index Page
    path('', index_view, name='index'),

    # Profile Data
    path('profile/', account_view, name='profile'),

    # Authentication and Authorization
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),

]
