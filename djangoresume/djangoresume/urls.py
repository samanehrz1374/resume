
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('mnresumeadmin/', admin.site.urls),
    path('resumesite/',include('resumesite.urls')),
    path('accounts/',include('accounts.urls'))
]
