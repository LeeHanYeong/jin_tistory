from django.urls import path

from members.views import register

urlpatterns = [
    path('register/', register, name='register')
]