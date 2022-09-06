from django.db import models
from django.db.models.fields import EmailField

class Reservation (models.Model):
    Nom_Client = models.CharField(max_length=50,blank=False, default="NomClient")
    Email = models.EmailField(max_length=50,blank=False)
    Prix_payer = models.FloatField(blank=False, default=1)
    Date = models.DateField(blank=False)
    Matricule = models.CharField(max_length=50, blank=False) 
    Periode_une = models.BooleanField(blank=False)
    Periode_deux = models.BooleanField(blank=False)
    Periode_trois = models.BooleanField(blank=False)
    Periode_quatre = models.BooleanField(blank=False)
    Periode_cinq = models.BooleanField(blank=False)
    Periode_six = models.BooleanField(blank=False)
    Periode_sept = models.BooleanField(blank=False)
    Periode_huit = models.BooleanField(blank=False)
    Lavage = models.BooleanField(blank=False)

    

    def __str__(self):
        return self.Email

