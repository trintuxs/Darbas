from django.db.models import Sum
from gyventojas.models import Resident, Flat
from administracija.models import Kaupiamasis_Inasas, Staff
from django.core.mail import send_mail
from datetime import date


def siusti_menesine_ataskaita():
    # Paimame šios dienos datą
    today = date.today()

    # Tikriname, ar šiandien yra mėnesio 8 diena
    if today.day == 6:
        # Gauname visus Kaupiamasis_Inasas objektus šiam mėnesiui
        kaupiamasis_inasas_objects = Kaupiamasis_Inasas.objects.all()

        # Skaičiuojame mėnesinį sąskaitos sumavimą
        bendras_inasas = sum(kaupiamasis_inasas.calculate_size() for kaupiamasis_inasas in kaupiamasis_inasas_objects)

        # Gauname visus darbuotojus
        darbuotojai = Staff.objects.all()

        # Skaičiuojame bendrą darbuotojų atlyginimų sumą
        bendra_atlyginimu_suma = darbuotojai.aggregate(total_wages=Sum('wage'))['total_wages'] or 0
        flat_owner = Flat.objets()
        flats = Flat.objects.filter(owner=flat_owner)

        number_of_flats = flats.count()
        if number_of_flats > 0:
            savininkui = bendra_atlyginimu_suma / number_of_flats
        else:
            savininkui = 0
        

        # Ruosiamas el. laiško turinys su mėnesio ataskaita
        zinute = f"Mėnesio ataskaita:\n\n"
        zinute += f"Bendras mėnesinis sąskaitos sumavimas: {bendras_inasas} eur\n\n"
        zinute += f"Darbuotojų atlyginimų paskirstymas už būtus:\n"
        for darbuotojas in darbuotojai:
            zinute += f"{darbuotojas.duties}: {savininkui} eur\n"

        # Siunčiame el. laišką visiems gyventojams, kurių el. pašto adresas nustatytas
        nuo_el_pastas = 'ilgoji4bendrija@gmail.com'
        gyventojai_su_el_pastu = Resident.objects.exclude(email='').values_list('email', flat=True)

        # Temos pavadinimas
        tema = 'Mėnesinė ataskaita'

        send_mail(tema, zinute, nuo_el_pastas, gyventojai_su_el_pastu)
