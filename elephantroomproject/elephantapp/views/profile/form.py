from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic
from elephantapp.models import Profile
from elephantapp.models import Category
from ..connection import Connection

# DO not know why I was doing this here, but everything seem sto function without it currrently. Don't want to delete it just yet.
# @login_required
# def get_profiles(request):
#     if request.method == 'GET':
#         current_user = request.user
#         current_profile_user = Profile.objects.get(user_id=current_user.id)
#         all_topics = Topic.objects.all()
#         all_profiles = Category.objects.all()
#         template = 'profiles/form.html'
#         context = {
#             'all_topics': all_topics,
#             'all_profiles': all_profiles
#         }

#         return render(request, template, context)
    
@login_required
def profile_form(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        profile = Profile.objects.all()
        template = 'profiles/form.html'
        context = {
            'profile': profile,
        }

        return render(request, template, context)
    
@login_required
def profile_edit_form(request, profile_id):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user__id=current_user.id)
        profile = Profile.objects.get(pk=profile_id)
        template = 'profiles/form.html'
        context = {
            'profile': profile,
        }

        return render(request, template, context)