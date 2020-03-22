from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Profile
from ..connection import Connection

def profile_list(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.filter(user_id=current_user.id)
        all_profiles = Profile.objects.all()
        
        profile_id = request.GET.get('profile_id', None)
        print(profile_id)        
        # if profile_id is not None:
        #     all_profiles = all_profiles.filter(profile_id__contains=profile_id)
    
        template = 'profiles/list.html'
        context = {
            'all_profiles': all_profiles
        }

        return render(request, template, context)