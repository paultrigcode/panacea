"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from CRUD.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',employee_list,name='employee_list'),
    path('<int:id>/details/',employee_details,name="employee_details"),
    path('<int:id>/edit',employee_edit,name='employee_edit'),
    path('add/',employee_add,name='employee_add'),
    path('<int:id>/delete',employee_delete,name='employee_delete'),

]
