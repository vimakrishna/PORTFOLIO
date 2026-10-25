"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.AboutView.as_view()),
    path('education/',views.educationView.as_view()),
    path('proj/',views.projectView.as_view()),
    path('skill/',views.skillsView.as_view()),
    path('exp/',views.experienceView.as_view()),
    path('certificate/',views.certificateView.as_view()),
    path('serv/',views.sevicesView.as_view())              
]

