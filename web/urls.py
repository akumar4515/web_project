from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user-profile/', views.userProfile , name='user-profile'),
    path('update-profile/', views.edit_profile, name='update-profile'),
    path('contact/', views.contact, name='contact'),
    path('adminX/', views.adminX, name='adminX'),
    path('admin-msg/', views.admin, name='admin-msg'),
    path('contX/', views.contX, name='contX'),
    path('topic/<int:courses_id>/', views.topic, name='topic'),
    path('sub_topic/<int:courses_id>/topics/<int:topic_id>/', views.subtopic, name='sub_topic'),
    path('content/<int:courses_id>/topics/<int:topic_id>/subtopic/<int:sub_topic_id>/', views.content, name='content')

]