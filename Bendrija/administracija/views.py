from django.db.models import Sum
from django.shortcuts import render

from gyventojas.models import Flat
from .models import Kaupiamasis_Inasas, Expenses, Staff


def index(request):
    # Gauti visus butus, priklausančius šiam vartotojui
    flats = Flat.objects.filter(owner=request.user)

    # Gauti visus butų kaupiamojo inaso objektus, priklausančius šiems butams
    kaupiamasis_inasas_objects = Kaupiamasis_Inasas.objects.filter(flat_owner__owner=request.user)

    # Apskaičiuoti bendrą visų butų inasų sumą
    total_inasas = kaupiamasis_inasas_objects.aggregate(total_size=Sum('flat_owner__size_kv'))['total_size'] or 0

    # Gauti visas išlaidas
    expenses = Expenses.objects.all()

    # Apskaičiuoti bendras išlaidas
    total_expenses = expenses.aggregate(total=Sum('repairs_cost'))['total'] or 0

    # Apskaičiuoti likutį
    balance = total_inasas - total_expenses

    # Gauti visus darbuotojus
    staff = Staff.objects.all()

    # Apskaičiuoti darbuotojų atlyginimų sumą
    total_wages = staff.aggregate(total_wages=Sum('wage'))['total_wages'] or 0

    # Padalinti darbuotojų atlyginimus iš butų skaičiaus
    number_of_flats = flats.count()
    if number_of_flats > 0:
        wage_per_flat = total_wages / number_of_flats
    else:
        wage_per_flat = 0

    context = {
        'kaupiamasis_inasas_objects': kaupiamasis_inasas_objects,
        'total_inasas': total_inasas,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'balance': balance,
        'staff': staff,
        'wage_per_flat': wage_per_flat,
        'total_wages': total_wages,
    }

    return render(request, 'buto_inasas.html', context=context)

'''
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'buto_inasas.html', {'staff': staff})

'''

