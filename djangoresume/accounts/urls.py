from django.urls import path
from accounts import views
from djangoresume import  settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('login/',views.loginVeiw),
    path('loginpanel/',views.loginpanelview),
    path('logout/',views.logoutVeiw),
    path('profileregister/',views.profileRegisterView),
    path('profile/',views.profileView)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)