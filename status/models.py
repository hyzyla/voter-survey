from django.db import models
from django_mysql.models import DynamicField


StatusTypes = [(1, "число"), (2, "рядок")]


class Status(models.Model):
    name = models.CharField(max_length=4096, verbose_name="назва")
    type = models.PositiveSmallIntegerField(choices=StatusTypes, verbose_name="тип")
    stations = models.ManyToManyField("territory.PollingStation", blank=True, related_name="statuses", verbose_name="дільниці")
    is_static = models.NullBooleanField(default=None, null=True, verbose_name="статичне поле?")
    #options = DynamicField(spec={}, null=False, blank=False)

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статуси"

    def __str__(self):
        return f"{self.name}"


class Option(models.Model):
    value = models.CharField(max_length=1024, verbose_name="значення")
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="options", verbose_name="статус")

    class Meta:
        verbose_name = "варіант"
        verbose_name_plural = "варіанти"