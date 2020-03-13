from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    relationship_status = models.CharField(max_length=55)
    political_affiliation = models.CharField(max_length=25)
    evidential_preference = models.CharField(max_length=25)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    debate_style_preference = models.CharField(max_length=25)
    avatar_image = models.CharField(max_length=100)
    theological_affiliation = models.CharField(max_length=50)
    is_online = models.BooleanField()
    is_neutral_chaotic = models.BooleanField()
    

    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
    
            return reverse("Profile_detail", kwargs={"pk": self.pk})

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
        if created:
                Profile.objects.create(user=instance)
                