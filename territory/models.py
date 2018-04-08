from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=2048)
    city = models.CharField(max_length=2048, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.city, self.region)



class Constituency(models.Model):
    name = models.CharField(max_length=2048)
    description = models.CharField(max_length=8192, blank=True, null=True)
    year = models.PositiveIntegerField(null=True)
    stations = models.ManyToManyField("PollingStation", related_name="constituencies")
    #region = models.ForeignKey("Region", on_delete=models.CASCADE, related_name='constituencies')


    def __str__(self):
        return f"{self.name}, {self.year}"


class PollingStation(models.Model):
    number = models.CharField(max_length=256)
    description = models.TextField(null=True)
    address = models.CharField(max_length=2048, null=True)
    is_deprecated = models.BooleanField(default=False)
    district = models.ForeignKey("District", null=True, on_delete=models.SET_NULL, related_name='stations')
    #consituency = models.ForeignKey("Constituency", null=True, on_delete=models.SET_NULL, related_name='constituencies')

    def __str__(self):
        return f"{self.number}, {self.district}"
