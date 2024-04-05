from django import forms
from .models import prediction

class MyForm(forms.ModelForm):
  class Meta:
    model = prediction
    fields = ['Farmer_name', 'location', 'contact', 'Date', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x9', 'x10', 'x11', 'PC', 'PN', 'PP', 'PK']#,"image"#, "image":"image"
    #labels = { 'Farmer_name': "Farmer_name", 'x1':"x1", 'x2':"x2", 'x3':"x3", 'x4':"x4", 'x5':"x5", 'x6':"x6", 'T|sub:x2':"x7", 'H|sub:x3':"x8", 'N|sub:x4':"x9", 'P|sub:x5':"x10", 'K|sub:x6':"x11"}
"""
class CropForm(forms.ModelForm):
  class Meta:
    model = prediction
    fields = [ "x12","x13","x14","x15","x16","x17","x18","x19","x20","x21","x22","x23"]

"""