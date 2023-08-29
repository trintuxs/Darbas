from django.db import models
from gyventojas.models import Resident


class Diskusija(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    text = models.TextField(verbose_name="Turinys")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0, verbose_name="Patiko")
    dislikes = models.PositiveIntegerField(default=0, verbose_name="Nepatiko")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Diskusija'
        verbose_name_plural = 'Diskusijos'

class Komentaras(models.Model):
    diskusija = models.ForeignKey('Diskusija', on_delete=models.CASCADE)
    gyventojas = models.ForeignKey(Resident, on_delete=models.CASCADE)
    turinys = models.TextField(verbose_name="Turinys")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Resident.first_name} {self.Resident.last_name}: {self.turinys}"

    class Meta:
        verbose_name = 'Komentaras'
        verbose_name_plural = 'Komentarai'

class Balsavimas(models.Model):
    vartotojas = models.ForeignKey(Resident, on_delete=models.CASCADE)
    diskusija = models.ForeignKey(Diskusija, on_delete=models.CASCADE)
    patiko = models.BooleanField(default=False)  # True - jei patiko, False - jei nepatiko

    class Meta:
        unique_together = ('vartotojas', 'diskusija')
