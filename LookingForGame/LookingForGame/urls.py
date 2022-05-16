"""LookingForGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views as core_views
from user import views as user_views

urlpatterns = [
    path('', core_views.index),
    path('profile/', core_views.profile),
    path('profile/groupview/<int:id>', core_views.profile_groupview),
    path('profile/delete/<int:id>', core_views.profile_del),
    path('about/', core_views.about_us),
    path('lfg/', core_views.lfg),
    path('lfg/<int:id>', core_views.lfg_group),
    path('lfg/sort_a/<str:age>', core_views.sort_age),
    path('lfg/sort_p/<str:players>', core_views.sort_players),
    path('lfg/sort_e/<str:exp>', core_views.sort_exp),
    path('admin/', admin.site.urls),
    path('join/', core_views.join),
    path('login/', core_views.user_login),
    path('logout/', core_views.user_logout),
    path('create_group/', core_views.create_group),
    path('user/', user_views.user),
    path('preferences/', user_views.preferences),
    path('profile/groupview/Group/<str:pk>/', core_views.group_page, name='room'),
    path('inbox/', user_views.ListThreads.as_view(), name='inbox'),
    path('inbox/new', user_views.CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', user_views.ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message', user_views.CreateMessage.as_view(), name='create-message'),
]
