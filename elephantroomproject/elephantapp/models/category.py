from django.db import models
from django.contrib.auth.models import User
from .topic import Topic
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    """
    Description: This is a class that creates a category it is made to be a holder for topics.
    FK: user_id: id from user to give unique identifier
    
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length= 25)
    blurb = models.CharField(max_length= 50)
    category_icon = models.CharField(max_length= 50)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
