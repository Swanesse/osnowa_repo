from django.db import models
from django.utils import timezone

class Point(models.Model):
    autor = models.ForeignKey('auth.User')
    arkusz_mapy = models.TextField()
    nazwa = models.TextField()
    klasa = models.TextField()
    numer = models.CharField(max_length=200)
    wojewodztwo = models.TextField()
    powiat = models.TextField()
    gmina = models.TextField()
    miejscowosc = models.TextField()
    stabilizacja = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    find_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa
