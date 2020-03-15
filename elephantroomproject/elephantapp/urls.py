from django.urls import path
from .views import *

app_name = "elephantapp"

urlpatterns = [
    path('', home, name='home'),
    path('topics/', topic_list, name='topics'),
]