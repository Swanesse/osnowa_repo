from django.db import models
from django.utils import timezone

class Point(models.Model):
    autor = models.ForeignKey('auth.User')
    arkusz_mapy = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)
    klasa = models.CharField(max_length=200)
    numer = models.CharField(max_length=200)
    wojewodztwo = models.CharField(max_length=200)
    powiat = models.CharField(max_length=200)
    gmina = models.CharField(max_length=200)
    miejscowosc = models.CharField(max_length=200)
    stabilizacja = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    find_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.find_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa
