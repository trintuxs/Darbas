from django.shortcuts import render
from .models import Kaupiamasis_Inasas, Expenses, Staff

def index(request):
    # Gauti visus Kaupiamasis_Inasas objektus
    kaupiamasis_inasas_objects = Kaupiamasis_Inasas.objects.filter(flat_owner__owner=request.user)

    # Apskaičiuoti bendrą visų butų inasų sumą
    total_inasas = sum(kaupiamasis_inasas.calculate_size() for kaupiamasis_inasas in kaupiamasis_inasas_objects)

    # Gauti visas išlaidas
    expenses = Expenses.objects.all()

    # Apskaičiuoti bendras išlaidas
    total_expenses = sum(expense.repairs_cost for expense in expenses)

    # Apskaičiuoti likutį
    balance = total_inasas - total_expenses

    # Gauti visus darbuotojus
    staff = Staff.objects.all()

    # Apskaičiuoti darbuotojų atlyginimų sumą
    total_wages = sum(staff_member.wage for staff_member in staff)

    # Padalinti darbuotojų atlyginimus iš butų skaičiaus
    if len(kaupiamasis_inasas_objects) > 0:
        wage_per_flat = total_wages / len(kaupiamasis_inasas_objects)
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

