from django.db import models


class Feature(models.Model):

    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Feature_detail", kwargs={"pk": self.pk})
