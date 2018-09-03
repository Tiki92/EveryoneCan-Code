from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<code_id>\d+)/$', views.detailed),
#    path("search",views.search, name="search"),

]