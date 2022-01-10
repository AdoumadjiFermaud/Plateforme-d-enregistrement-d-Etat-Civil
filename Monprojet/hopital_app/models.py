from django.db import models


    
class Acte(models.Model):
    numero_acte = models.IntegerField('Numero Acte')

    
class Declaration(models.Model):
    declaration = models.TextField('Declaration', max_length=120)
    

class Pere(models.Model):
    nom_pere = models.CharField('Nom',max_length=120)
    date_de_naissance = models.DateField('Date de Naissance')
    lieu_de_naissance = models.CharField('Lieu de Naissance', max_length=120)
    fonction = models.CharField('Fonction', max_length=120)
    login = models.CharField('Login', max_length=120)
    password =models.CharField ('Password', max_length=120)
    tel = models.CharField('Tel', max_length=120)
    
class Mere(models.Model):
    nom_mere = models.CharField('Nom de Mere', max_length= 12)
    date_de_naissance = models.DateField('Date de Naissance')
    lieu_de_naissance = models.CharField('Lieu de Naissance', max_length=120)
    fonction = models.CharField('Fonction', max_length=120)
    login = models.CharField('Login', max_length=120)
    password =models.CharField ('Password', max_length=120)
    tel = models.CharField('Tel', max_length=120)
    
    
class Enfant(models.Model):
    nom = models.CharField('Nom', max_length= 120)
    prenom = models.CharField('Prenom', max_length= 120)
    date_de_naissance = models.DateField('Date de Naissance')
    lieu_de_naissance = models.CharField('Lieu de Naissance', max_length= 120)
    num_social = models.IntegerField ('Numero Social')
    num_declaration = models.IntegerField('Numero Declaration')
    sexe = models.CharField('Sexe',max_length= 120)
    acte = models.ForeignKey(Acte,blank=False, null=False, on_delete=models.CASCADE)
    pere = models.ForeignKey(Pere, blank=False, null=False, on_delete=models.CASCADE)
    mere = models.ForeignKey(Mere, blank=False, null=False, on_delete=models.CASCADE)
    
   
    def __str__(self):
        return self.Enfant
    
class Accouchement(models.Model):
    nombre_naissance = models.IntegerField('Nombre_naissance')
    mode_accouchement = models.CharField('Mode_accouchement', max_length=20)
    enfant = models.ForeignKey(Enfant, blank=False, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Accouchement


class Adjoint(models.Model):
    nom = models.CharField('Nom',max_length= 120)
    login = models.CharField ('Login',max_length= 30)
    password = models.CharField('Password', max_length= 12)
    signature = models.CharField('Signature', max_length= 50)
    cachet = models.CharField('Cachet', max_length= 120)
    tel = models.CharField('Tel', max_length= 120)
    
    
 
    
class Infirmier(models.Model):
    nom = models.CharField('Nom', max_length=120)
    tel = models.CharField('Tel',max_length= 120)
    password = models.CharField('Password',max_length=120)
    login = models.CharField('Login', max_length= 120)
    accouchement = models.ForeignKey(Accouchement,blank=False, null=False, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.Infirmier 
    
    
class Hopital(models.Model):
    nom_hopital = models.CharField('Nom', max_length= 120)
    adress_hopital = models.CharField ('Adresse de Hopital', max_length= 120)
    ville = models.CharField('Ville', max_length= 120)
    declaration = models.ForeignKey(Declaration,blank=False, null=False, on_delete=models.CASCADE )
    infirmier = models.ForeignKey(Infirmier,blank=False, null=False, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.Hopital
    
class Secretaire(models.Model):
    nom = models.CharField('Nom', max_length= 120)
    tel = models.CharField('Tel',max_length=112)
    password = models.CharField('Password',max_length=102)
    login = models.CharField ('Login',max_length= 130)
    cachet = models.CharField ('Cachet',max_length=120)
    signature = models.CharField('Signature',max_length=120)
    
class Officier(models.Model):
    nom = models.CharField('Nom', max_length= 120)
    password = models.CharField('Password',max_length=120)
    login = models.CharField('Login', max_length=120)
    cachet = models.CharField('Cachet', max_length=120)
    signature = models.CharField('Signature',max_length=120)
    
class Mairie(models.Model):
    nom = models.CharField('Nom', max_length= 120)
    tel = models.CharField('Tel',max_length= 120)
    logo = models.CharField('Logo',max_length=120)
    declaration = models.ForeignKey(Declaration, blank=False , null=False, on_delete=models.CASCADE)
    adjoint = models.ForeignKey(Adjoint,blank=False , null=False, on_delete=models.CASCADE )
    officier = models.ForeignKey(Officier, blank=False , null=False, on_delete=models.CASCADE)
    secretaire = models.ForeignKey(Secretaire, blank=False , null=False, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.Mairie
    
    