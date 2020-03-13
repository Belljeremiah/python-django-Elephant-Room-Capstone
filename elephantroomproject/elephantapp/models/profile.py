from django.db import models

class Profile(models.Model):

    age = models.IntegerField()
    relationship_status = models.CharField(max_length=55)
    political_affiliation = models.CharField()
    evidential_preference = models.CharField()
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    debate_style_preference = models.CharField()
    avatar_image = models.CharField()
    theological_affiliation = models.CharField()
    is_online = models.BooleanField()
    is_neutral_chaotic = models.BooleanField()
    

    class Meta:
        verbose_name = ("profile"  
        )
        verbose_name_plural = ("profiles")

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
    
            return reverse("Profile_detail", kwargs={"pk": self.pk})
