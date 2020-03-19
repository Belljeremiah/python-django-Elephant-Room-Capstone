from django.db import models
from django.contrib.auth.models import User
from .category import Category


class Topic(models.Model):
    """
    description: This class creates a Topic which is the main object of data I use for this app.
    
    
    """    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=25, default=None, null=True)
    stance_text_body = models.CharField(max_length=100, default=None, null=True)
    is_anecdote = models.BooleanField(default=False, null=True)
    is_citable = models.BooleanField(default=False, null=True)
    blurb = models.CharField(max_length=100, default=None, null=True)
    resource_link = models.CharField(max_length=100, default=None, null=True)
    image_link = models.CharField(max_length=100, default=None, null=True)
    is_free_resource = models.BooleanField(default=False, null=True)
    is_proponent = models.BooleanField(default=False, null=True)
    anecdote_body = models.CharField(max_length=3000, default=None, null=True)
    # user = models.models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)("Employee", through='EmployeeComputer')

    class Meta:
        verbose_name = ("topic")
        verbose_name_plural = ("topics")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"pk": self.pk})
