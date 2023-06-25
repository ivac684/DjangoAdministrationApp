from django import forms
from .models import Korisnici, Predmeti, Upisi

class KorisniciForm(forms.ModelForm):
    class Meta:
        model = Korisnici
        fields = ['username', 'email', 'password', 'role', 'status']

class PredmetiForm(forms.ModelForm):
    class Meta:
        model = Predmeti
        fields = '__all__'

class AssignSubjectForm(forms.Form):
    professor = forms.ModelChoiceField(queryset=Korisnici.objects.filter(role='prof'))
    subject = forms.ModelChoiceField(queryset=Predmeti.objects.all())

class UpisiForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Predmeti.STATUS)

    class Meta:
        model = Upisi
        fields = ('status',)