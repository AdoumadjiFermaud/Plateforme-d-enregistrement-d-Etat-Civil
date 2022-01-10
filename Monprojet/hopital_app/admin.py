from django.contrib import admin
from .models import Enfant, Mere, Pere,Declaration, Mere, Acte, Adjoint, Secretaire,Officier,Mairie,Accouchement,Hopital,Infirmier


@admin.register(Enfant)
class EnfantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_de_naissance', 'lieu_de_naissance', 'num_social', 'num_declaration', 'sexe', 'acte', )
    ordering = ('nom', )
    search_fields =  ('nom', )


@admin.register(Mere)
class MereAdmin(admin.ModelAdmin):
    list_display = ('nom_mere', 'date_de_naissance', 'fonction',)
    ordering = ('nom_mere', )
    search_fields =  ('nom_mere', )
    

@admin.register(Pere)
class PereAdmin(admin.ModelAdmin):
    list_display = ('nom_pere', 'date_de_naissance','lieu_de_naissance', 'login', 'password', 'fonction', 'enfant','tel', )
    ordering = ('nom_pere', )
    search_fields =  ('fonction', )
    
@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
    list_display = ('declaration',)
    ordering = ('declaration', )
    search_fields =  ('declaration', )

@admin.register(Acte)
class ActeAdmin(admin.ModelAdmin):
    list_display = ('numero_acte',)
    ordering = ('numero_acte', )
    search_fields =  ('numero_acte', )

@admin.register(Adjoint)
class AdjointAdmin(admin.ModelAdmin):
    list_display = ('nom', 'login', 'password','signature', 'cachet','tel', )
    ordering = ('nom', )
    search_fields =  ('signature', )

@admin.register(Secretaire)
class SecretaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tel', 'password','cachet', 'signature', 'login', )
    ordering = ('nom', )
    search_fields =  ('signature',)

@admin.register(Officier)
class OfficierAdmin(admin.ModelAdmin):
    list_display = ('nom', 'password', 'login', 'cachet' , 'signature' ,)
    ordering = ('nom', )
    search_fields =  ('signature', )

@admin.register(Mairie)
class MairieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tel', 'logo', 'declaration', 'adjoint' , 'officier', 'secretaire' , )
    ordering = ('nom', )
    search_fields =  ('logo', )
    
    
@admin.register(Accouchement)
class AccouchementAdmin(admin.ModelAdmin):
    list_display = ('nombre_naissance', 'mode_accouchement', 'enfant', )
    ordering = ('mode_accouchement', )
    search_fields =  ('enfant', )



@admin.register(Hopital)
class HopitalAdmin(admin.ModelAdmin):
    list_display = ('nom_hopital', 'adress_hopital', 'ville', 'declaration' , 'infirmier' , )
    ordering = ('nom_hopital', )
    search_fields =  ('ville', )
    
@admin.register(Infirmier)
class InfirmierAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tel', 'accouchement', 'password' , 'login' , )
    ordering = ('nom', )
    search_fields =  ('tel', )




