from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Topic
from elephantapp.models import Profile
from elephantapp.models import Category
from ..connection import Connection

@login_required
def topic_list(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        all_topics = Topic.objects.all()
        
        title = request.GET.get('title', None)
                
        if title is not None:
            all_topics = all_topics.filter(title__contains=title)
        
        template = 'topics/list.html'
        context = {
            'all_topics': all_topics
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        current_user = request.user
        associated_category = Category.objects.filter(id=associated_category.id)
        form_data = request.POST

        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT INTO elephantapp_topic
        #     (
        #         title, stance_text_body, is_anecdote,
        #         is_citable, user_id, blurb, resource_link,
        #         image_link, is_free_resource, is_proponent
        #     )
        #     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        #     """,
        #     (form_data['title'], form_data['stance_text_body'], form_data['is_anecdote'], 
        #         form_data['is_citable'], current_user.id, form_data['blurb'], form_data['resource_link'],
        #         form_data['image_link'], form_data['is_free_resource'], form_data['is_proponent']))
        is_proponent_boolean = False
        is_proponent = 'is_proponent' in request.POST
        if is_proponent == True : is_proponent_boolean = True
        
        is_anecdote_boolean = False
        is_anecdote = 'is_anecdote' in request.POST
        if is_anecdote == True : is_anecdote_boolean = True
        
        is_citable_boolean = False
        is_citable = 'is_citable' in request.POST
        if is_citable == True : is_citable_boolean = True
        
        is_free_resource_boolean = False
        is_free_resource = 'is_free_resource' in request.POST
        if is_free_resource == True : is_free_resource_boolean = True
        
        
        new_topic = Topic.objects.create(
            title = form_data['title'],
            stance_text_body = form_data['stance_text_body'],
            is_anecdote = is_anecdote_boolean, 
            is_citable = is_citable_boolean, 
            user_id = current_user.id, 
            blurb = form_data['blurb'], 
            resource_link = form_data['resource_link'],
            image_link = form_data['image_link'],
            is_free_resource = is_free_resource_boolean,
            category_id = form_data['category'],
            is_proponent = is_proponent_boolean,
            anecdote_body = form_data['anecdote_body']
        )
        
        return redirect(reverse('elephantapp:topics'))