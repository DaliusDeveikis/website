from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets

from .models import Service, Intro
from .serializers import IntroSerializer, ServiceSerializer


class HomeView(View):
    def get(self, request, *args, **kwargs):
        intros = Intro.objects.all().filter(is_active=True)
        services = Service.objects.all().filter(is_active=True)
        data = {
            'intros': intros,
            'services': services,
        }
        return render(request, 'pages/index.html', data)


def privacy(request):
    return render(request, 'pages/privacy-policy.html')


def terms(request):
    return render(request, 'pages/terms-conditions.html')


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().filter(is_active=True)


class IntroViewSet(viewsets.ModelViewSet):
    serializer_class = IntroSerializer
    queryset = Intro.objects.all().filter(is_active=True)
