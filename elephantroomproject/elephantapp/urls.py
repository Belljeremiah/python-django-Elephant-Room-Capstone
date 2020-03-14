from django.urls import path
from .views import *

app_name = "elephantapp"

urlpatterns = [
    path('', topic_list, name='home'),
    path('topics/', topic_list, name='topics'),
]