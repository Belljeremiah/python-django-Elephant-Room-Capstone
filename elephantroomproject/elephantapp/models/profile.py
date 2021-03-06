from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(None, null=True)
    relationship_status = models.CharField(max_length=55, null=True)
    political_affiliation = models.CharField(max_length=25, null=True)
    evidential_preference = models.CharField(max_length=25, null=True)
    debate_style_preference = models.CharField(max_length=25, null=True)
    avatar_image = models.CharField(max_length=100, null=True)
    theological_affiliation = models.CharField(max_length=50, null=True)
    is_online = models.BooleanField(null=True)
    is_neutral_chaotic = models.BooleanField(null=True)
    

    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
    
            return reverse("Profile_detail", kwargs={"pk": self.pk})
                