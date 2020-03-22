from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category, Profile
from ..connection import Connection

@login_required
def profile_details(request, profile_id):
    
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.filter(user_id=current_user.id)
        profile = Profile.objects.get(pk=profile_id)
        print(profile.id)
        
        template = 'profiles/detail.html'
        context = {
            'profile': profile
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'PUT'
        ):

            profile_to_update = Profile.objects.get(id=profile_id)
            
            profile_to_update.age = form_data['age']
            profile_to_update.relationship_status = form_data['relationship_status']
            profile_to_update.political_affiliation = form_data['political_affiliation']
            profile_to_update.evidential_preference = form_data['evidential_preference']
            profile_to_update.debate_style_preference = form_data['debate_style_preference']
            profile_to_update.avatar_image = form_data['avatar_image']
            profile_to_update.theological_affiliation = form_data['theological_affiliation']
            
            profile_to_update.save()
            
            return redirect(reverse('elephantapp:profiles'))