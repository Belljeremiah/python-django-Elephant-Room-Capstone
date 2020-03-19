from django.urls import path
from django.conf.urls import include
from .views import *
from .views.auth.logout import logout_user
from .views.register import register_user

app_name = "elephantapp"
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('topics/', topic_list, name='topics'),
    path('profiles/', profile_list, name='profiles'),
    path('categories/', category_list, name='categories'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name="register"),
    path('topic/form', topic_form, name='topic_form'),
    path('category/form', category_form, name='category_form')
]