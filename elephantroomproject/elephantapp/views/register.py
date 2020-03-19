from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from elephantapp.models import Profile
from .connection import Connection

@csrf_exempt
def register(request):
    """View method for handling creation of a new user for auth
        Args:
        request = full http object
    """
    
    if request.method == 'GET':
        profiles = Profile.objects.all()
        
        template = 'registration/register.html'
        context = {
            'all_profiles': profiles
        }
        
        return render(request, template, context)
    # For handling when user submits the form data
    elif request.method == "POST":
        form_data = request.POST

        # First create a new user using django's built in craziness. create_user is a method in django.
        new_user = User.objects.create_user(
            username=form_data['username'],
            email=form_data['email'],
            password=form_data['password'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name']
        )

        # Second, make a profile after the user has been created
        profile = Profile.objects.create(
            user=new_user,
            # If you have other form data to save on the new profile, that isn't a property of the User model...
            age=form_data['age'],
            relationship_status=form_data['relationship_status'],
            political_affiliation=form_data['political_affiliation'],
            evidential_preference=form_data['evidential_preference'],
            debate_style_preference=form_data['debate_style_preference'],
            avatar_image=form_data['avatar_image'],
            theological_affiliation=form_data['theological_affiliation']
        )
        # new_user = authenticate(username=form_data['username'], password=form_data['password']),
        
        login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
        return redirect(reverse('elephantapp:profiles'))

    # handles a request to load the empty form for the useer to fill out
    else:
        template = 'registration/register.html'

    return render(request, template, {})