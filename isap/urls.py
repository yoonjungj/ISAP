from django.urls import path
from isap import views

urlpatterns = [
    path("", views.index, name='index')
]