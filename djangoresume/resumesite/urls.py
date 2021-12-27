from django import urls
from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from .views import aboutmeview

router=routers.DefaultRouter()
router.register('aboutme',views.aboutmeview)

urlpatterns = [
    path('',views.home),
    path('fa/',views.fahome),
    path('api/',include(router.urls))
]
