from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category, Profile
from ..connection import Connection

@login_required
def topic_details(request, topic_id):
    
    if request.method == 'GET':
        topic = Topic.objects.get(id=topic_id)
        print(topic.id)
        
        template = 'topics/detail.html'
        context = {
            'topic': topic
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'DELETE'
        ):
            topic = Topic.objects.get(id=topic_id)
            topic.delete()
            
            return redirect(reverse('elephantapp:topics'))
        
    elif request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'PUT'
        ):
        
            topic_to_update = Topic.objects.get(id=topic_id)
            
            topic_to_update.title = form_data['title']
            topic_to_update.stance_text_body = form_data['stance_text_body']
            topic_to_update.is_anecdote = form_data['is_anecdote']
            topic_to_update.is_citable = form_data['is_citable']
            topic_to_update.blurb = form_data['blurb']
            topic_to_update.resource_link = form_data['resource_link']
            topic_to_update.image_link = form_data['image_link']
            topic_to_update.is_free_resource = form_data['title']
            topic_to_update.is_proponent = form_data['is_proponent']
            topic_to_update.anecdote_body = form_data['anecdote_body']
            topic_to_update.category_id = form_data['category_id']
            
            topic_to_update.save()
            
            return redirect(reverse('elephantapp:topics'))