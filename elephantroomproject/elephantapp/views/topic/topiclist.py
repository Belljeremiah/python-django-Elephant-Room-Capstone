import sqlite3
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Topic
from elephantapp.models import Profile
from elephantapp.models import Category
from ..connection import Connection

def topic_list(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            select
                t.id,
                t.title,
                t.stance_text_body,
                t.is_anecdote,
                t.is_citable,
                t.blurb,
                t.resource_link,
                t.image_link,
                t.is_free_resource,
                t.is_proponent
            from elephantapp_topic t
            """)
            
            # setting object to a container []
            all_topics = []
            dataset = db_cursor.fetchall()
            
            for row in dataset:
                topic = Topic()
                topic.id = row['id']
                topic.title = row['title']
                topic.stance_text_body = row['stance_text_body']
                topic.is_anecdote = row['is_anecdote']
                topic.is_citable = row['is_citable']
                topic.blurb = row['blurb']
                topic.resource_link = row['resource_link']
                topic.image_link = row['image_link']
                topic.is_free_resource = row['is_free_resource']
                topic.is_proponent = row['is_proponent']

                all_topics.append(topic)
                
        template = 'topics/list.html'
        context = {
            'all_topics': all_topics
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO elephantapp_topic
            (
                title, stance_text_body, is_anecdote,
                is_citable, user_id, blurb, resource_link,
                image_link, is_free_resource, is_proponent
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['stance_text_body'],
                form_data['is_anecdote'], form_data['is_citable'],
                current_user.id, form_data['blurb'], form_data['resource_link'],
                form_data['image_link'], form_data['is_free_resource'], form_data['is_proponent']))

        return redirect(reverse('elephantapp:topics'))