"""
URL configuration for crop_prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crop.views import Contact, Index, results, cropData, Data, report, my_form, confirm
#from crop.views import compare
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns  

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('reports/', report, name='report'),
    path('results/', results, name='results'),
    path('analysis/', confirm, name='analysis'),
    path('cropData/', cropData ,name='cropData'),
    path('contact/', Contact.as_view(), name='contact'),
    path('Data/', Data.as_view(), name='Data'),
    path('retrive/', my_form, name='retrive'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()