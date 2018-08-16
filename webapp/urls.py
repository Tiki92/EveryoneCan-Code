from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('webapp/Post', views.post_code, name='post_code'),
]git