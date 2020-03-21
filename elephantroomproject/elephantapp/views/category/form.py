from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic
from elephantapp.models import Profile
from elephantapp.models import Category
from ..connection import Connection

# @login_required
# def get_categories(request):
#     if request.method == 'GET':
#         current_user = request.user
#         current_profile_user = Profile.objects.get(user_id=current_user.id)
#         all_topics = Topic.objects.all()
#         all_categories = Category.objects.all()
#         template = 'categories/form.html'
#         context = {
#             'all_topics': all_topics,
#             'all_categories': all_categories
#         }

#         return render(request, template, context)
    
@login_required
def category_form(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        category = Category.objects.all()
        template = 'categories/form.html'
        context = {
            'category': category,
        }

        return render(request, template, context)
    
@login_required
def category_edit_form(request, category_id):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user__id=current_user.id)
        category = Category.objects.get(pk=category_id)
        template = 'categories/form.html'
        context = {
            'category': category,
        }

        return render(request, template, context)