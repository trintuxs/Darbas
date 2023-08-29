from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .forms import KomentarasForm, DiskusijaForm
from .models import Diskusija, Balsavimas, Komentaras



@login_required
def diskusija_detail(request, diskusija_id):
    diskusija = get_object_or_404(Diskusija, pk=diskusija_id)
    komentarai = Komentaras.objects.filter(diskusija=diskusija)
    return render(request, 'diskusija_detail.html', {'diskusija': diskusija, 'komentarai': komentarai})


from .models import Diskusija

def visos_diskusijos(request):
    diskusijos = Diskusija.objects.all()
    return render(request, 'visos_diskusijos.html', {'diskusijos': diskusijos})


@login_required
def kurti_diskusija(request):
    if request.method == 'POST':
        form = DiskusijaForm(request.POST)
        if form.is_valid():
            pavadinimas = form.cleaned_data['pavadinimas']
            turinys = form.cleaned_data['turinys']
            nauja_diskusija = Diskusija(title=pavadinimas, text=turinys)
            nauja_diskusija.save()
            return redirect('diskusija_detail', diskusija_id=nauja_diskusija.id)
    else:
        form = DiskusijaForm()
    return render(request, 'kurti_diskusija.html', {'form': form})

@login_required
def balsuoti_diskusija(request, diskusija_id):
    diskusija = Diskusija.objects.get(pk=diskusija_id)
    vartotojas = request.user

    # Patikrinkite, ar vartotojas jau balsavo už šią diskusiją
    try:
        balsavimas = Balsavimas.objects.get(vartotojas=vartotojas, diskusija=diskusija)
    except Balsavimas.DoesNotExist:
        balsavimas = None

    if balsavimas is None:
        # Vartotojas dar nebuvo balsavęs, todėl jis gali balsuoti
        patiko = request.POST.get('patiko') == 'true'  # Šis žymės ar vartotojas paspaudė "patiko"

        # Sukurkite naują įrašą Balsavimas modelyje
        balsavimas = Balsavimas(vartotojas=vartotojas, diskusija=diskusija, patiko=patiko)
        balsavimas.save()

        # Atnaujinkite Diskusija modelį pagal naują balsavimo rezultatą
        if patiko:
            diskusija.likes += 1
        else:
            diskusija.dislikes += 1
        diskusija.save()

    # Nukreipkite vartotoją į diskusijos detalės puslapį
    return redirect('diskusija_detail', diskusija_id=diskusija_id)



@login_required
def prideti_komentara(request, diskusija_id):
    diskusija = get_object_or_404(Diskusija, pk=diskusija_id)

    if request.method == 'POST':
        form = KomentarasForm(request.POST)
        if form.is_valid():
            komentaro_turinys = form.cleaned_data['turinys']
            komentaras = Komentaras(diskusija=diskusija, gyventojas=request.user, turinys=komentaro_turinys)
            komentaras.save()

    # Nukreipkite vartotoją atgal į diskusijos detalės puslapį
    return redirect('diskusija_detail', diskusija_id=diskusija_id)

