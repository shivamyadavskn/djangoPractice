"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from practice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="home"),
    path('about/',views.about,name="about"),
    path('freelancer/',views.freelancer,name="freelancer"),
    path('job/',views.job,name="job"),
    path('form/',views.form,name="form"),
    path('userform/',views.userform,name="userform"),
    path('newdemo/<slug>',views.newDemo),
    path('filters/',views.filterData),
    
]
