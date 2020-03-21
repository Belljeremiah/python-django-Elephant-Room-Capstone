from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category, Profile
from ..connection import Connection

@login_required
def category_details(request, category_id):
    
    if request.method == 'GET':
        current_user = request.user
        current_profile_user = Profile.objects.get(user_id=current_user.id)
        category = Category.objects.get(pk=category_id)
        print(category.name)
        
        template = 'categories/detail.html'
        context = {
            'category': category
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'DELETE'
        ):
            category = Category.objects.get(id=category_id)
            category.delete()
            
            return redirect(reverse('elephantapp:categories'))
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'PUT'
        ):

            category_to_update = Category.objects.get(id=category_id)
            
            category_to_update.name = form_data['name']
            category_to_update.blurb = form_data['blurb']
            category_to_update.category_icon = form_data['category_icon']
            
            category_to_update.save()
            
            return redirect(reverse('elephantapp:categories'))