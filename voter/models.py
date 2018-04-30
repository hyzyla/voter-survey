from django.db import models
from django_mysql.models import DynamicField
from django.contrib.auth.models import User


# Create your models here.
class Voter(models.Model):
    station = models.ForeignKey("territory.PollingStation", on_delete=models.CASCADE, verbose_name="дільниця")
    attrib = DynamicField(spec={}, null=False, blank=False)
    operators = models.ManyToManyField(User, related_name="voters")

    class Meta:
        verbose_name = "виборець"
        verbose_name_plural = "виборці"

    def __str__(self):
        return f"{self.pk}"
