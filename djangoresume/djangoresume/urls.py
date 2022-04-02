
from django.contrib import admin
from django.urls import path , include
from django.conf import  settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('mnresumeadmin/', admin.site.urls),
    path('',include('resumesite.urls')),
    path('accounts/',include('accounts.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
