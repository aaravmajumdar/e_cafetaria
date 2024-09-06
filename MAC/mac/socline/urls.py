from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    # path('search', views.search, name='search'),
    # path('blogHome', views.blogHome, name='blogHome'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('server',views.serverHome, name="ServerHome"),
    path('server/<str:slug>', views.ServerRoom, name="Server"),
    path('postMessage', views.PostMessage, name="postMessage"),

    # path('blog/', include('blog.urls')),

]