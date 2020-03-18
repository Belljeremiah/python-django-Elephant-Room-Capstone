import sqlite3
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Category
from elephantapp.models import Topic
from elephantapp.models import Profile
from ..connection import Connection

def category_list(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()
            
        #     db_cursor.execute("""
        #     select
        #         c.id,
        #         c.user_id,
        #         c.topic_id,
        #         c.name,
        #         c.blurb,
        #         c.category_icon
        #     from elephantapp_category c
        #     """)
            
        #     # setting object to a container []
        #     all_categories = []
        #     dataset = db_cursor.fetchall()
            
        #     for row in dataset:
        #         category = Category()
        #         category.id = row['id']
        #         category.user_id = row['user_id']
        #         category.topic_id = row['topic_id']
        #         category.name = row['name']
        #         category.blurb = row['blurb']
        #         category.category_icon = row['category_icon']

        #         all_categories.append(category)
        all_categories = Category.objects.all()
        
        name = request.GET.get('name', None)
        
        if name is not None:
            all_categories = all_categories.filter(name__contains=name)
                
        template = 'categories/list.html'
        context = {
            'all_categories': all_categories
        }

        return render(request, template, context)

    elif request.method == 'POST':
            current_user = request.user
            current_profile_user = Profile.objects.get(user_id=current_user.id)
            all_topics = Topic.objects.all(user_id=current_user.id)
            # The wrong way to grab topic ids. above is the hopefully correct new way I am trying.
            # current_topic = request.topic
            # user_topic_id = Topic.objects.get(id=current_topic.id)
            form_data = request.POST

            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #     INSERT INTO elephantapp_topic
            #     (
            #         user_id,
            #         topic_id,
            #         name, 
            #         blurb, 
            #         category_icon,
            #     )
            #     VALUES (?, ?, ?, ?, ?)
            #     """,
            #     (current_user.id, 
            #     topic_id, 
            #     form_data['name'], 
            #     form_data['blurb'],
            #     form_data['category_icon']))
            
            new_category = Category.objects.create(
                user_id = current_user.id,
                topic_id = all_topics,
                name = form_data['name'],
                blurb = form_data['blurb'],
                category_icon = form_data['category_icon']
            )

            return redirect(reverse('elephantapp:categories'))