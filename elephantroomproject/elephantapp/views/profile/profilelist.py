import sqlite3
from django.shortcuts import render
from elephantapp.models import Profile
from ..connection import Connection

def profile_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            select
                p.id,
                p.user_id,
                p.age,
                p.relationship_status,
                p.political_affiliation,
                p.evidential_preference,
                p.debate_style_preference,
                p.avatar_image,
                p.theological_affiliation
            from elephantapp_profile p
            """)
            
            # setting object to a container []
            all_profiles = []
            dataset = db_cursor.fetchall()
            
            for row in dataset:
                profile = Profile()
                profile.id = row['id']
                profile.user_id = row['user_id']
                profile.relationship_status = row['relationship_status']
                profile.political_affiliation = row['political_affiliation']
                profile.evidential_preference = row['evidential_preference']
                profile.debate_style_preference = row['debate_style_preference']
                profile.avatar_image = row['avatar_image']
                profile.theological_affiliation = row['theological_affiliation']

                all_profiles.append(profile)
                
        template = 'profiles/list.html'
        context = {
            'all_profiles': all_profiles
        }

        return render(request, template, context)