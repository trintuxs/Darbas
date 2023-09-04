
from django.shortcuts import render
from django.views import generic


from .models import Resident, Flat





def index(request):
    rezident = Resident.objects.count()
    flats = Flat.objects.count()
    context = {
        'rezident': rezident,
        'flats': flats
    }
    return render(request, 'index.html', context=context)


def residents(request):
    residents = Resident.objects.all()
    return render(request, 'gyventojas.html', {'gyventojas': residents})


class ResidentListView(generic.ListView):
    model = Resident
    template_name = 'gyventoju_sarasas.html'

def flat(request):
    flat = Flat.objects.all()
    context = {
        'butas': flat
    }
    print(flat)
    return render(request, 'butas.html', context)

