
from django.shortcuts import render
from django.views import generic


from .models import Resident, Flat
'''
@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

'''





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

'''
def prisijungimas(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('index')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})
'''