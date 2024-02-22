"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from company.views import EmpView, TeamView
from django.urls import path, include
from lab5.views import EmployeeAPIView, TeamViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EmpView),
    path('create-team/', TeamView.as_view(), name='create_team'),
    path('api-auth/', include('rest_framework.urls')),
    path('employee/', EmployeeAPIView.as_view(), name='employee-list-create'),
    path('employee/<int:pk>/', EmployeeAPIView.as_view(), name='employee-update'),
    path('employee/<int:pk>/', EmployeeAPIView.as_view(), name='employee-delete'),
    path('teams/', include(router.urls)),
    
]
     

