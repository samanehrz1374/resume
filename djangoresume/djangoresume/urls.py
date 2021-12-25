
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('mnresumeadmin/', admin.site.urls),
    path('',include('resumesite.urls')),
]
