"""
URL configuration for ramtant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

import users.views as u
import features.views as f
import posts.views as p

account_patterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', u.Reg.as_view(), name='register')
]

profile_patterns = [
    path('user/<str:username>/', u.profile, name='profile'),
    path('user/<str:username>/follow', u.follow, name='follow'),
    path('user/<str:username>/unfollow', u.unfollow, name='unfollow'),
    path('user/', u.profile, name='my_profile'),
    path('edit/', u.profile_edit, name='profile_edit')
]

post_patterns = [
    path('list', p.post_list, name='post_list'),
    path('write', p.post_create, name='post_create'),
    path('<int:post_id>/', p.post_detail, name='post_detail'),
    path('<int:post_id>/delete/', p.post_delete, name='post_delete'),
    path('<int:post_id>/edit/', p.post_edit, name='post_edit'),
    path('search/', p.post_search, name='post_search')
]

urlpatterns = [
    path('', f.index),
    path('index', f.index),
    path('admin/', admin.site.urls),
    path('account/', include(account_patterns)),
    path('profile/', include(profile_patterns)),
    path('posts/', include(post_patterns))
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)