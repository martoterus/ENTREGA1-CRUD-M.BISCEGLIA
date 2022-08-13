from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Appventas/', include("Appventas.urls")),
    path('',include("Appventas.urls"))
    
   
]
