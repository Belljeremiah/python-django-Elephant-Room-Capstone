import sqlite3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from elephantapp.models import Category
from elephantapp.models import Profile
from ..connection import Connection

@login_required
def category_list(request):
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.filter(user_id=current_user.id)
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
            form_data = request.POST
            
            new_category = Category.objects.create(
                user_id = current_user.id,
                name = form_data['name'],
                blurb = form_data['blurb'],
                category_icon = form_data['category_icon']
            )

            return redirect(reverse('elephantapp:categories'))