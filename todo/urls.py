"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home import views as home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.TaskListView.as_view(), name='home'),
    path('new', home_view.TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update', home_view.TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', home_view.TaskDeleteView.as_view(), name='task-delete'),
    # This is overridden by above path
    path('', home_view.home, name='home'),
]
