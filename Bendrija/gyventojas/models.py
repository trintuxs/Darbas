from django.contrib.auth.models import AbstractUser
from django.db import models

# Sukuriame Flat modelį
class Flat(models.Model):
    flat_nr = models.CharField(max_length=10)  # Laukas flat_nr
    size_kv = models.FloatField(verbose_name="kv")  # Laukas size_kv
    owner = models.ForeignKey('Resident', on_delete=models.SET_NULL, null=True, blank=True, related_name='butai')  # Laukas owner, nurodantys, kad jis yra Resident modelio ForeignKey

    def __str__(self):
        return f"{self.flat_nr} {self.size_kv} {self.owner}"

    class Meta:
        verbose_name = 'Butas'
        verbose_name_plural = 'Butai'

# Sukuriame Resident modelį, paveldintį iš AbstractUser
class Resident(AbstractUser):
    flat_nr = models.ForeignKey(Flat, on_delete=models.SET_NULL, null=True, blank=True, related_name='gyventojas')  # Laukas flat_nr, nurodantys ForeignKey į Flat modelį

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.flat_nr} {self.email}"

    class Meta:
        verbose_name = 'Gyventojas'
        verbose_name_plural = 'Gyventojai'