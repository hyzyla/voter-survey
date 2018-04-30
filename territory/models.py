from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=1024, verbose_name="назва")

    class Meta:
        verbose_name = "область"
        verbose_name_plural = "області"

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=2048, verbose_name="назва")
    city = models.CharField(max_length=2048, null=True, verbose_name="місто")
    region = models.ForeignKey("Region", on_delete=models.CASCADE, related_name='districts', verbose_name="область")

    class Meta:
        verbose_name = "район"
        verbose_name_plural = "райони"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.city, self.region)



class Constituency(models.Model):
    name = models.CharField(max_length=2048, verbose_name="назва")
    description = models.CharField(max_length=8192, blank=True, null=True, verbose_name="опис")
    year = models.PositiveIntegerField(null=True, verbose_name="рік")
    stations = models.ManyToManyField("PollingStation", related_name="constituencies", verbose_name="дільниці")
    #region = models.ForeignKey("Region", on_delete=models.CASCADE, related_name='constituencies')

    class Meta:
        verbose_name = "округ"
        verbose_name_plural = "округи"

    def __str__(self):
        return f"{self.name}, {self.year}"


class PollingStation(models.Model):
    number = models.CharField(max_length=256, verbose_name="номер")
    description = models.TextField(null=True, verbose_name="опис")
    address = models.CharField(max_length=2048, null=True, verbose_name="адреса")
    is_deprecated = models.BooleanField(default=False, verbose_name="не активна?")
    district = models.ForeignKey("District", null=True, on_delete=models.SET_NULL, related_name='stations', verbose_name="район")
    #consituency = models.ForeignKey("Constituency", null=True, on_delete=models.SET_NULL, related_name='constituencies')

    class Meta:
        verbose_name = "дільниця"
        verbose_name_plural = "дільниці"

    def __str__(self):
        return f"{self.number}, {self.district}"
