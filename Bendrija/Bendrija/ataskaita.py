from gyventojas.models import Resident
from administracija.models import Kaupiamasis_Inasas, Staff
from django.core.mail import send_mail
from datetime import date


def siusti_menesine_ataskaita():
    # Paimame šios dienos datą
    today = date.today()

    # Tikriname, ar šiandien yra mėnesio 8 diena
    if today.day == 8:
        # Gauname visus Kaupiamasis_Inasas objektus šiam mėnesiui
        kaupiamasis_inasas_objects = Kaupiamasis_Inasas.objects.all()

        # Skaičiuojame mėnesinį sąskaitos sumavimą
        bendras_inasas = sum(kaupiamasis_inasas.calculate_size() for kaupiamasis_inasas in kaupiamasis_inasas_objects)

        # Gauname visus darbuotojus
        darbuotojai = Staff.objects.all()

        # Skaičiuojame bendrą darbuotojų atlyginimų sumą
        bendra_atlyginimu_suma = sum(darbuotojas.wage for darbuotojas in darbuotojai)

        # Skaičiuojame atlyginimą už butą
        if len(kaupiamasis_inasas_objects) > 0:
            atlyginimas_uz_buta = bendra_atlyginimu_suma / len(kaupiamasis_inasas_objects)
        else:
            atlyginimas_uz_buta = 0

        # Ruosiamas el. laiško turinys su mėnesio ataskaita
        zinute = f"Mėnesio ataskaita:\n\n"
        zinute += f"Bendras mėnesinis sąskaitos sumavimas: {bendras_inasas} eur\n\n"
        zinute += f"Darbuotojų atlyginimų paskirstymas už būtus:\n"
        for darbuotojas in darbuotojai:
            zinute += f"{darbuotojas.duties}: {atlyginimas_uz_buta} eur\n"

        # Siunčiame el. laišką visiems gyventojams, kurių el. pašto adresas nustatytas
        nuo_el_pastas = 'ilgoji4bendrija@gmail.com'
        gyventojai_su_el_pastu = Resident.objects.exclude(email='').values_list('email', flat=True)

        # Temos pavadinimas
        tema = 'Mėnesinė ataskaita'

        send_mail(tema, zinute, nuo_el_pastas, gyventojai_su_el_pastu)
