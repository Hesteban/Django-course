from django.urls import path
from second_app import views

app_name = 'second_app'

urlpatterns = [
    path('users', views.users, name='users'),
    path('signup', views.signup, name='signup')
]