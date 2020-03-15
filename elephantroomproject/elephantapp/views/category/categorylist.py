import sqlite3
from django.shortcuts import render
from elephantapp.models import Category
from ..connection import Connection

def category_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            select
                c.id,
                c.user_id,
                c.topic_id,
                c.name,
                c.blurb,
                c.category_icon
            from elephantapp_category c
            """)
            
            # setting object to a container []
            all_categories = []
            dataset = db_cursor.fetchall()
            
            for row in dataset:
                category = Category()
                category.id = row['id']
                category.user_id = row['user_id']
                category.topic_id = row['topic_id']
                category.name = row['name']
                category.blurb = row['blurb']
                category.category_icon = row['category_icon']

                all_categories.append(category)
                
        template = 'categories/list.html'
        context = {
            'all_categories': all_categories
        }

        return render(request, template, context)