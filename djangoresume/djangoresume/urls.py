
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('mnresumeadmin/', admin.site.urls),
    path('',include('resumesite.urls')),
    path('',include('accounts.urls'))
]
