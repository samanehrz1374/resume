from django.urls import path
from accounts import views
from django.conf import  settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/',views.loginVeiw),
    path('loginpanel/',views.loginpanelview),
    path('logout/',views.logoutVeiw),
    path('profileregister/',views.profileRegisterView),
    path('profile/',views.profileView),
    path('profileEdit/',views.ProfileEditView),
    path('resumeprofile/',views.resumeprofileview)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)