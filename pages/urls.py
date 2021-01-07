from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ServiceViewSet, IntroViewSet, HomeView

router = routers.DefaultRouter()
router.register('services', ServiceViewSet)
router.register('intro', IntroViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', include(router.urls)),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
]
