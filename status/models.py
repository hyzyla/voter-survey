from django.db import models
from django_mysql.models import DynamicField


StatusTypes = [(1, "число"), (2, "рядок")]


class Status(models.Model):
    name = models.CharField(max_length=4096)
    type = models.PositiveSmallIntegerField(choices=StatusTypes)
    stations = models.ManyToManyField("territory.PollingStation", blank=True, related_name="statuses")
    is_static = models.NullBooleanField(default=None, null=True)
    #options = DynamicField(spec={}, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Option(models.Model):
    value = models.CharField(max_length=1024)
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="options")