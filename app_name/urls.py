from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

#Add Django site authentication urls (for login, logout, password management)
