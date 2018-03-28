from django.db import models
from django_mysql.models import DynamicField


# Create your models here.
class Voter(models.Model):
    station = models.ForeignKey("territory.PollingStation", on_delete=models.CASCADE)
    attrib = DynamicField(spec={}, null=False, blank=False)

    def __str__(self):
        return f"{self.pk}"
