
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from gyventojas.models import Resident


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Resident
        fields = ('username', 'email')  # Naudojame 'username' ir 'email' laukus iš modelio


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Resident
        fields = ('username', 'email', 'flat_nr')  # Naudojame 'username' ir 'email'

'''
class loginForm(forms.Form):
    username = forms.CharField(label='vartotojo vardas', max_length=100)
    password = forms.CharField(label='slaptazodis')
'''