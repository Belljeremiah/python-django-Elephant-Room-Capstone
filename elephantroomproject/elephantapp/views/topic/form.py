import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic
from elephantapp.models import Category
from ..connection import Connection


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
        categories = get_categories()
        template = 'topics/form.html'
        context = {
            'all_categories': categories
        }

        return render(request, template, context)