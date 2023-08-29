from django import forms


class KomentarasForm(forms.Form):
    turinys = forms.CharField(widget=forms.Textarea)



class DiskusijaForm(forms.Form):
    pavadinimas = forms.CharField(max_length=100, label="Pavadinimas")
    turinys = forms.CharField(widget=forms.Textarea, label="Turinys")