from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Topic
from elephantapp.models import Profile
from elephantapp.models import Category
from ..connection import Connection

@login_required
def topic_list(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.filter(user=current_user)
        all_topics = Topic.objects.filter(user=current_user)
        all_categories = Category.objects.filter(user=current_user)
        
        title = request.GET.get('title', None)
                
        if title is not None:
            all_topics = all_topics.filter(title__contains=title)
        
        template = 'topics/list.html'
        context = {
            'all_topics': all_topics,
            'all_categories': all_categories
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        current_user = request.user
        form_data = request.POST
        
        proponent_boolean = form_data.get("is_proponent", False)
        anecdote_boolean = form_data.get("is_anecdote", False)
        citable_boolean = form_data.get("is_citable", False)
        free_resource_boolean = form_data.get("is_free_resource", False)
        
        new_topic = Topic.objects.create(
            title = form_data['title'],
            stance_text_body = form_data['stance_text_body'],
            is_anecdote = anecdote_boolean, 
            is_citable = citable_boolean, 
            user_id = current_user.id, 
            blurb = form_data['blurb'], 
            resource_link = form_data['resource_link'],
            image_link = form_data['image_link'],
            is_free_resource = free_resource_boolean,
            category_id = form_data['category'],
            is_proponent = proponent_boolean,
            anecdote_body = form_data['anecdote_body']
        )
        
        return redirect(reverse('elephantapp:topics'))
        
        