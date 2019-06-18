"""untitled URL Configuration

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
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_138/', views.test_138),
    path('test_148/', views.test_148),
    path('test_158/',views.test_158),
    path('test_168/',views.test_168),
    path('test__148/',views.test__148),
    path('test__158/',views.test__158),
    path('test__168/',views.test__168),
    path('meinian/',views.meinian),
    path('yinchuan',views.yinchuan),
    path('nalong',views.nalong),
    path('sumer/',views.sumer),
]
