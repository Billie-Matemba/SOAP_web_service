from django.contrib import admin
from django.urls import path
from soap_service.views import meter_confirmation_endpoint 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meter/confirm/', meter_confirmation_endpoint, name='meter-confirmation'),  
]