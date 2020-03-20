from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category
from ..connection import Connection

@login_required
def category_details(request, category_id):
    
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        print(category.title)
        
        template = 'categories/detail.html'
        context = {
            'category': category
        }
        
        return render(request, template, context)