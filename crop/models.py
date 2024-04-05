from django.db import models
from django.utils import timezone
# Create your models here.
class cropInfo(models.Model):
    name = models.CharField(max_length=100)
    ph = models.CharField(max_length=100, blank=True)
    H = models.CharField(max_length=100)
    T = models.CharField(max_length=100)
    N = models.CharField(max_length=100)
    P = models.CharField(max_length=100)
    K = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
   


class prediction(models.Model):
    Farmer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    x1 = models.CharField(max_length=100)
    x2 = models.CharField(max_length=100)
    x3 = models.CharField(max_length=100)
    x4 = models.CharField(max_length=100)
    x5 = models.CharField(max_length=100)
    x6 = models.CharField(max_length=100)
    x9 = models.CharField(max_length=100)
    x10 = models.CharField(max_length=100)
    x11 = models.CharField(max_length=100)
    PC = models.CharField(max_length=100, blank=True)
    PN = models.CharField(max_length=100, blank=True)
    PP = models.CharField(max_length=100, blank=True)
    PK = models.CharField(max_length=100, blank=True)
    
  #  image = models.ImageField(upload_to='images/',blank=True)

    


    def __str__(self):
        return self.Farmer_name
    
"""
class Thershold(models.Model):
    R_Nthers = models.CharField(max_length=100)
    R_Pthers = models.CharField(max_length=100)
    R_Kther = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

"""