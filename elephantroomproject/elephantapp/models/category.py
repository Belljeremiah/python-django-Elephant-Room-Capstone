from django.db import models

class Category(models.Model):
    """
    Description: This is a class that creates a category it is made to be a holder for topics.
    FK: user_id: id from user to give unique identifier
    
    """

    name = models.CharField(max_length= 25)
    blurb = models.CharField(max_length= 50)
    topic_id = models.IntegerField()
    category_icon = models.CharField(max_length= 50)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
