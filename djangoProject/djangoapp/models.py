from django.db import models


# Create your models here.
class Temp(models.Model):
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.pk} {self.message}"


