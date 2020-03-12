from django.db import models

class Topic(models.Model):

    

    class Meta:
        verbose_name = ("topic")
        verbose_name_plural = ("topics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"pk": self.pk})
