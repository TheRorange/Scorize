from django.shortcuts import render
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from .serializers import UniversitySerializer
from .models import University

class UniversityListAPI(generics.ListAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'city', 'city__country']
    ordering_fields = ['city', 'city__country']

    # cache for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class UniversityDetailAPI(generics.ListAPIView):
    serializer_class = UniversitySerializer
    
    def get_queryset(self, **kwargs):
        return University.objects.filter(id=self.kwargs.get('id', ''))
    
    # cache for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
