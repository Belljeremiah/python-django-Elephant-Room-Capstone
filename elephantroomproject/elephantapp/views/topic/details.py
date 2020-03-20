from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category
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