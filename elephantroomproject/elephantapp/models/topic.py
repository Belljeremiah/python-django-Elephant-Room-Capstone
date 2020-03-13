from django.db import models

class Topic(models.Model):
    """
    description: This class creates a Topic which is the main object of data I use for this app.
    
    
    """    
    
    title = models.CharField(max_length=25, default=None, null=True)
    stance_text_body = models.CharField(max_length=100, default=None, null=True)
    is_anecdote = models.BooleanField()
    is_citable = models.BooleanField()
    blurb = models.CharField(max_length=100, default=None, null=True)
    resource_link = models.CharField(max_length=100, default=None, null=True)
    image_link = models.CharField(max_length=100, default=None, null=True)
    is_free_resource = models.BooleanField()
    is_proponent = models.BooleanField()
    # user = models.models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)("Employee", through='EmployeeComputer')

    class Meta:
        verbose_name = ("topic")
        verbose_name_plural = ("topics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"pk": self.pk})
