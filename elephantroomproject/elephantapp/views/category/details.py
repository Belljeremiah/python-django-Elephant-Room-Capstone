from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category
from ..connection import Connection

@login_required
def category_details(request, category_id):
    
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
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