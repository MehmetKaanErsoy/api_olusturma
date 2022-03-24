from django.db import models


# Create your models here.

class Urun(models.Model):
    urun_ismi = models.CharField(max_length=100)
    urun_tur = models.CharField(max_length=50)

    def __str__(self):
        return self.urun_ismi + " " + self.urun_tur
