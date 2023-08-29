from django.db import models
from gyventojas.models import Flat

class Kaupiamasis_Inasas(models.Model):
    flat_owner = models.ForeignKey(Flat, on_delete=models.SET_NULL, null=True, blank=True, related_name='kaupiamasis_inasas')
    payment_rate = models.FloatField(verbose_name="Mokėjimo koeficientas")

    def __str__(self):
        return f"Kaupiamasis Inasas ({self.flat_owner})"

    class Meta:
        verbose_name = 'Kaupiamasis Inasas'
        verbose_name_plural = 'Kaupiamieji Inasai'

    def calculate_size(self):
        if self.flat_owner and self.flat_owner.size_kv:
            return self.flat_owner.size_kv * self.payment_rate
        return 0.0

    # Mėnesio inasas yra tas pats kaip ir viso inasas
    def calculate_monthly_inasas(self):
        return self.calculate_size()

    # Bendras visu inasas
    def calculate_total_inasas(self):
        kaupiamasis_inasas_objects = Kaupiamasis_Inasas.objects.all()
        total_inasas = sum(kaupiamasis_inasas.calculate_size() for kaupiamasis_inasas in kaupiamasis_inasas_objects)

        return total_inasas


class Expenses(models.Model):
    description = models.CharField(max_length=255, verbose_name="Islaidu aprasymas")
    repairs_cost = models.FloatField(verbose_name="Islaidu suma")
    date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    month = models.CharField(max_length=7) #galimes atsekti kada buvo islaidos anksciau
    def __str__(self):
        return f"{self.description} {self.repairs_cost}"

    class Meta:
        verbose_name = 'Islaidos'
        verbose_name_plural = 'Islaidos'

     # Metodas, kuris apskaičiuoja išlaidų sumą, atimtą iš bendros visų butų inasų sumos


def calculate_total_expenses(self):
    # Gauti visus Kaupiamasis_Inasas objektus
    kaupiamasis_inasas_objects = Kaupiamasis_Inasas.objects.all()

    # Apskaičiuoti bendrą visų butų inasų sumą
    total_inasas = sum(kaupiamasis_inasas.calculate_size() for kaupiamasis_inasas in kaupiamasis_inasas_objects)

    # Gauti self.repairs_cost lauko reikšmę ir konvertuoti į float
    repairs_cost = float(self.repairs_cost)

    # Apskaičiuoti išlaidų sumą
    total_expenses = total_inasas - repairs_cost

    return total_expenses


class Staff(models.Model):
    duties = models.CharField(max_length=255)
    wage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.duties} {self.wage} "

    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = 'Darbuotojai'
