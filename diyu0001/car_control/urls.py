from django.conf.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name='index'),
    re_path(r'^action/(?P<car_forward>[\w]+)/$',views.car_action,name='car_action'), 
]
