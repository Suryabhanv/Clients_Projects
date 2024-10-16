"""client_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse

# Simple home view
def home_view(request):
    return HttpResponse("<h1>Welcome to the Client Project API</h1>")
from clientapp.views import ClientListCreateView, ClientRetrieveUpdateDestroyView, ProjectCreateView, UserAssignedProjectsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('api/', include('clientapp.urls')),  # This includes your app's URLs
]

