from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from elephantapp.models import Topic, Category
from ..connection import Connection

@login_required
def category_details(category_id):
    category = Category.objects.get(id=category_id)
    print(category.title)
    
    template = 'category/detail.html'
    context = {
        'category': category
    }
    
    return render(request, template, context)