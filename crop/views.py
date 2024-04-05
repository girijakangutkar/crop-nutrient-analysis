from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import cropInfo
import serial
import time
import pickle
import os
from django.conf import settings
#from . import sensor as ard
# Create your views here.
from django.shortcuts import render
from .models import prediction
from .forms import MyForm#, CropForm
import random


def my_form(request):

    prediction_info = prediction.objects.all()
    context = {
        'prediction_info':prediction_info,
    }

    crop_data = cropInfo.objects.all()
    context = {
        'crop_data':crop_data,
    }

    if request.method == "POST":
        form = MyForm(request.POST)
       # cropform = CropForm(request.POST)
        if form.is_valid():
            form.save()
           # cropform.save()
    else:
      form = MyForm()
     # cropform = CropForm()
    Farmer_name = request.POST.get('Farmer_name')
    location = request.POST.get('location')
    contact = request.POST.get('contact')
    PC = request.POST.get('PC')
    PN = request.POST.get('PN')
    PP = request.POST.get('PP')
    PK = request.POST.get('PK')
    x1 = request.POST.get('x1')
    x2 = request.POST.get('x2')
    x3 = request.POST.get('x3')
    x4 = request.POST.get('x4')
    x5 = request.POST.get('x5')
    x6 = request.POST.get('x6')
    for x in crop_data:
        if x.name == x1:
            x7 = request.POST.get('x7')
            x8 = request.POST.get('x8')
            x9 = request.POST.get('x9')
            x10 = request.POST.get('x10')
            x11 = request.POST.get('x11')
    #x12 = request.POST.GET('X12')
    
       
    print(type(Farmer_name))
    print("name of farmer",Farmer_name)
    print(x2)
    print(x3)
    print(x4)
    print(x5)
    print(x6)
    for x in crop_data:
        if x.name == x1:
            print(x.name)
            print(x9)
            print(x10)
            print(x11)


    return render(request, 'form.html', {'form':form, 'location':location, 'contact':contact, 'Farmer_name':Farmer_name, 'PC':PC, 'PN':PN, 'PP':PP, 'PK':PK, 'x1':x1, 'x2':x2, 'x3':x3, 'x4':x4, 'x5':x5, 'x6':x6, 'x9':x9, 'x10':x10, 'x11':x11, 'prediction_info':prediction_info, 'crop_data':crop_data})
"""
    crop_info = cropInfo.objects.all()
    context = {
        'crop_info':crop_info,
    }
   
     




"""
   
"""
        'crop_mahiti':crop_mahiti,
    }


    , 'crop_mahiti':crop_mahiti

    

      def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
 """ 

class Index(View):
      def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
      
      



"""
class Index(View):
    def get(self, request, *args, **kwargs):
        ser=serial.Serial("com9",9600)
        data = []
        for i in range(6):
            b = ser.readline()
            string_n = b.decode()
            string =string_n.rstrip()
            flt = string
            data.append(string)
            time.sleep(0.1)
        ser.close()
        print(data)
        ser.close()
        return render(request, 'index.html', { 'read':data })
"""
class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')
    
class Data(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'data.html')
    
def cropData(request):
    crop_info = cropInfo.objects.all()
    context = {
        'crop_info':crop_info,
    }
    return render(request, 'crop.html', context)

def report(request):
    prediction_info = prediction.objects.all()
    context = {
        'prediction_info':prediction_info,
    }
    return render(request, 'report.html', context)

def results(request):
   
    crop_data = cropInfo.objects.all()
    context = {
        'crop_data':crop_data,
    }

    foo = ['Rice', 'Nachani', 'Kulith', 'Chavali', 'Kadave', 'Bhuimug']
    crp = random.choice(foo)
   
    crop = request.POST.get('crop')
    h = int(request.POST.get('H'))
    t = int(request.POST.get('T'))
    n = int(request.POST.get('N'))
    p = int(request.POST.get('P'))
    k = int(request.POST.get('K'))


    print(h)
    print(t)
    print(n)
    print(type(n))
    print(p)
    print(k)
        #retrive = prediction(crop=crop,H=h,T=t,N=n,P=p,K=k)
       # retrive.save
    return render(request, 'results.html', { 'H':h,'T':t, 'N':n, 'P':p, 'K':k, 'crop':crop, 'crop_data':crop_data, 'crp':crp })
"""
    if request.method=='POST':
        nitrogen=int(request.POST['N'])
        phosphorus=int(request.POST['P'])
        potassium=int(request.POST['K'])
        temperature=int(request.POST['T'],False)
        humidity=int(request.POST['H'])
        #ph=int(request.POST['ph'],False)

        with open(os.path.join(settings.BASE_DIR,'crop_rfc_model'),'rb') as f:
            model=pickle.load(f)
            print("model loaded ")
            result=model.predict([[nitrogen,phosphorus,potassium,temperature,humidity]])
            print("value predicted")

    #return render(request, 'results.html', {'result':result})  
"""

def confirm(request):
    crop_data = cropInfo.objects.all()
    context = {
        'crop_data':crop_data,
    }

    CN = request.POST.get('CN')
    g1 = request.POST.get('g1')
    g2 = int(request.POST.get('g2'))
    g3 = int(request.POST.get('g3'))
    g4 = int(request.POST.get('g4'))
    g5 = int(request.POST.get('g5'))
    g6 = int(request.POST.get('g6'))
    g7 = request.POST.get('g7')
    g10 = request.POST.get('g10')
    g11 = request.POST.get('g11')
    g12 = request.POST.get('g12')

    print(g1)
    print(g2)
    print(g3)
    print(g4)
    print(type(g4))
    print(g5)
    print(g6)
    print(g7)
    print(g10)
    print(g11)
    print(g12)

    return render(request, 'confirm.html', { 'CN':CN, 'g1':g1, 'g2':g2, 'g3':g3, 'g4':g4, 'g5':g5, 'g6':g6, 'g7':g7, 'g10':g10, 'g11':g11, 'g12':g12, 'crop_data':crop_data})

"""

    threshold={
    #RICE
    'R_N':range(85,100),
    'R_P':range(40,50),
    'R_K':range(40,50),
    #NACHANI
    'N_N':range(85,100),
    'N_P':range(40,50),
    'N_K':range(40,50),
    #KULITH
    'K_N':range(85,100),
    'K_P':range(40,50),
    'K_K':range(40,50),
    #CHAVALI
    'C_N':range(85,100),
    'C_P':range(40,50),
    'C_K':range(40,50),
    #KADAVE
    'W_N':range(85,100),
    'W_P':range(40,50),
    'W_K':range(40,50),
    #BHUIMUG
    'B_N':range(85,100),
    'B_P':range(40,50),
    'B_K':range(40,50),
}




    if request.method=='POST':
        nitrogen=int(request.POST['N'])
        phosphorus=int(request.POST['P'])
        potassium=int(request.POST['K'])
        temperature=int(request.POST['T'],False)
        humidity=int(request.POST['H'])
        ph=int(request.POST['ph'],False)

        with open(os.path.join(settings.BASE_DIR,'crop_rfc_model'),'rb') as f:
            model=pickle.load(f)
            print("model loaded ")
            result=model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph]])
            print("value predicted")

    return render(request, 'results.html', {'result':result})


    ph = request.POST.get('pH')
    h = request.POST.get('Humidity')
    t = request.POST.get('Temperature')
    n = request.POST.get('N')
    p = request.POST.get('P')
    k = request.POST.get('K')


    print(ph)
    print(t)
    print(h)
    print(n)
    print(p)
    print(k)
    'ph':ph, 'T':t, 'H':h, 'N':n, 'P':p, 'K':k ,'crop_data':crop_data
"""   
   # return render(request,'result.html',{'result':result})

 #   return render(request,'result.html',{'PH':ph, 'H':h, 'T':t, 'N':n, 'P':p, 'K':k, 'result':result})








  






 
   
    
 






       # for line in data:
       #    print(line)
       # read=ser.read().decode().strip()
      #  print(read)
        #read=ser.readline().decode().strip()

              #return render(request, 'index.html', { 'read':read })#ard.getsensordata() })  
