from django import forms
from django.forms import ModelForm
from .models import  Enfant


class EnfantForm(ModelForm):
    class Meta:
        model = Enfant
        fields = ( 
                  
                  'nom', 
                  'prenom',
                  'date_de_naissance',
                  'lieu_de_naissance', 
                  'num_social', 
                  'num_declaration',
                  'sexe', 
                  'acte', 
                  'pere',
                  'mere' , )

        labels = {
                        'nom': '',
                        'prenom': '',
                        'date_de_naissance': '',
                        'lieu_de_naissance': '', 
                        'num_social': '',  
                        'num_declaration': '',  
                        'sexe': '',  
                        'acte': 'Selectionner le père', 
                        'pere': 'Selectionner la mere',
                        'mere': 'Selectionner la mere', 
        }

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}),
            'date_de_naissance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date de naissance',}),
            'lieu_de_naissance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance',}),
            'num_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'numéro social',}),  
            'num_declaration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'numero de Déclaration',}),
            'sexe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre',}),
            'acte': forms.Select(attrs={'class': 'form-select', 'placeholder': "Choisir l'acte",}), 
            'pere': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choisir le Père',}),
            'mere': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choisir la Mère',}), 
        }

