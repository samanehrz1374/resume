
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('mndjangoadmin/', admin.site.urls),
    path('',include('resumesite.urls')),
]
