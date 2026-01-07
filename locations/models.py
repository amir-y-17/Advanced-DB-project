from django.db import models
from django_jalali.db import models as jmodels


class Province(models.Model):
    name = models.CharField(max_length=100)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name="cities"
    )
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.province.name}"


class Village(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="villages")
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.city.name}"
