from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('activate/account/', views.activate_account, name='activate'),
    path('register/', views.register, name='register'),
    path('password-change-done/',
        auth_views.password_change_done,
        {'template_name': 'cadmin/password_change_done.html'},
        name='password_change_done'
    ),
    path('password-change/',
        auth_views.password_change,
        {'template_name': 'cadmin/password_change.html', 
         'post_change_redirect': 'password_change_done'},
        name='password_change'
    ),

    path('', views.home, name='home'), 
    path('login/', views.login, 
          {'template_name': 'cadmin/login.html'}, name='login'),
    path('logout/', auth_views.logout, 
          {'template_name': 'cadmin/logout.html'}, name='logout'),
    path('post/add/', views.post_add, name='post_add'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'), 
]


