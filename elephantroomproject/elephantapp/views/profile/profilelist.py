from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Profile
from elephantapp.models import Category
from elephantapp.models import Topic
from ..connection import Connection


@login_required
def profile_list(request):
    if request.method == 'GET':
        current_user = request.user
        all_profiles = Profile.objects.filter(user=current_user)
        all_categories = Category.objects.filter(user=current_user)
        all_topics = Topic.objects.filter(user=current_user)
        
        profile_id = request.GET.get('profile_id', None)
        print(profile_id)        
        # if profile_id is not None:
        #     all_profiles = all_profiles.filter(profile_id__contains=profile_id)
    
        template = 'profiles/list.html'
        context = {
            'all_profiles': all_profiles,
            'all_categories': all_categories,
            'all_topics': all_topics
        }

        return render(request, template, context)