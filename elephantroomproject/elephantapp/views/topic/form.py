import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic
from elephantapp.models import Category
from ..connection import Connection


def get_topics():
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
            t.user_id,
            t.blurb,
            t.resource_link,
            t.image_link,
            t.is_free_resource,
            t.category_id,
            t.is_proponent
            
            
        from elephantapp_topic t
        """)

        return db_cursor.fetchall()
    
def get_categories():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.blurb
        from elephantapp_category c
        """)

        return db_cursor.fetchall()

@login_required
def topic_form(request):
    if request.method == 'GET':
        all_topics = get_topics()
        all_categories = get_categories()
        template = 'topics/form.html'
        context = {
            'all_topics': all_topics,
            'all_categories': all_categories
        }

        return render(request, template, context)