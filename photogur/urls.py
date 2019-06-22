"""photogur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from photogur.views import root, pictures_page, picture_show, picture_search, add_picture, edit_picture, user_pictures, create_comment, login_view, logout_view, signup

urlpatterns = [
    path('', root, name='root'),
    path('admin/', admin.site.urls),
    path('pictures/', pictures_page),
    path('pictures/<int:id>', picture_show, name='picture_details'),
    path('pictures/new', add_picture, name='add_picture'),
    path('pictures/edit/<int:id>', edit_picture, name='edit_picture'),
    path('pictures/user', user_pictures, name='user_pictures'),
    path('search', picture_search, name='picture_search'),
    path('comments/new', create_comment, name='create_comment'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
]
