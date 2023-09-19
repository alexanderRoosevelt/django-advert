from django.shortcuts import render

from rest_framework import generics
from .models import Advert
from .serializers import AdvertSerializer

class AdvertListAPIView(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

class AdvertDetailAPIView(generics.RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1  # Увеличиваем счетчик просмотров на 1
        instance.save()     # Сохраняем изменения в базе данных
        return super().retrieve(request, *args, **kwargs)
