from django.db import models
from django.db.models.fields import EmailField

class Parking (models.Model):
    Name = models.CharField(max_length=50,blank=False, default="NomParking")
    Nombre_Place = models.IntegerField(blank=False, default=1)
    Prix_Periode = models.FloatField(blank=False, default=1)
    Prix_Abonnement = models.FloatField(blank=False, default=60)
    Date_ouverture = models.DateField(blank=False)
    Date_fermeture = models.DateField(blank=False)
    Telephone = models.IntegerField(blank=False) 
    Email = models.EmailField(max_length=50,blank=False)
    Description = models.CharField(max_length=50,blank=True)
    

    def __str__(self):
        return self.Name
