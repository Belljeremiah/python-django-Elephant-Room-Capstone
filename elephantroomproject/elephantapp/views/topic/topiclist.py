import sqlite3
from django.shortcuts import render
from elephantapp.models import Topic
from elephantapp.views import Connection

def topic_list(request):
    if request.method == 'GET':
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