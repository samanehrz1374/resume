from django.urls import path
from accounts import views


urlpatterns = [
    path('login/',views.loginVeiw),
    path('loginpanel/',views.loginpanelview),
    path('logout/',views.logoutVeiw),
    path('profileregister/',views.profileRegisterView),
    path('profile/',views.profileView)
]