from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic
from elephantapp.models import Category
from elephantapp.models import Profile
from ..connection import Connection

@login_required
def topic_form(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        all_topics = Topic.objects.filter(user=current_user)
        all_categories = Category.objects.filter(user=current_user)
        template = 'topics/form.html'
        context = {
            'all_topics': all_topics,
            'all_categories': all_categories
        }

        return render(request, template, context)

@login_required
def topic_edit_form(request, topic_id):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user__id=current_user.id)
        topic = Topic.objects.get(pk=topic_id)
        all_categories = Category.objects.all()
        template = 'topics/form.html'
        context = {
            'topic': topic,
            'all_categories': all_categories
        }

        return render(request, template, context)