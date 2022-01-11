from django.urls import path
from accounts import views


urlpatterns = [
    path('login/',views.loginVeiw),
    # path('logout/',views.logoutVeiw)
]