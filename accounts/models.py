from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    scope = models.TextField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "نقش"
        verbose_name_plural = "نقش‌ها"


class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
