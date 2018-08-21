from django.urls import path
from . import views

urlpatterns = [
    path('Post/', views.post_code, name='index'),
]