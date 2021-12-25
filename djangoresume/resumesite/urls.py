from django.urls import path
from . import views

urlpatterns = [
    path('en/',views.home),
    path('fa/',views.fahome)
   
]
