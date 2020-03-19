from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from elephantapp.models import Profile

def register_user(request):
    """View method for handling creation of a new user for auth
        Args:
        request = full http object
    """

    # For handling when user submits the form data
    if request.method == "POST":

        # First create a new user using django's built in craziness. create_user is a method in django.
        new_user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )

        # Second, make a profile after the user has been created
        profile = Profile.objects.create(
            user=new_user,
            # If you have other form data to save on the new profile, that isn't a property of the User model...
            relationship_status=request.POST['relationship_status'],
            political_affiliation=request.POST['political_affiliation'],
            evidential_preference=request.POST['evidential_preference'],
            debate_style_preference=request.POST['debate_style_preference'],
            avatar_image=request.POST['avatar_image'],
            theological_affiliation=request.POST['theological_affiliation']
        )

        login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
        return redirect(reverse('elephantapp:profile'))

    # handles a request to load the empty form for the useer to fill out
    else:
        template = 'registration/register.html'

    return render(request, template, {})