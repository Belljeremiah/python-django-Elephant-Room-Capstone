from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category
from ..connection import Connection

def topic_details(topic_id):
    topic = Topic.objects.get(id=topic_id)
    print(topic.title)
    
    template = 'topic/detail.html'
    context = {
        'topic': topic
    }
    
    return render(request, template, context)