from django.urls import path
from account import views


urlpatterns = [
    path('login/',views.loginVeiw),
    path('logout/',views.logoutVeiw)
]