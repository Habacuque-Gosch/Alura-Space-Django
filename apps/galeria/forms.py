from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'fotos': forms.FileInput(attrs={'class': 'form-control'}),
            'salario': forms.TextInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type': 'date', 
                    'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'})
        }