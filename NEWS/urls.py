"""jayalathenterprises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from.import views
from .views import PostHomeView,PostDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,LikeView


urlpatterns = [
    # path("",views.home,name='home'),
    path('',PostHomeView.as_view(),name='home_news'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name='edit_post'),
    path('post/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('like/<int:pk>', LikeView,name='like_post')

]
