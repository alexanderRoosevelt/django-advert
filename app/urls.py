from django.urls import path
from .views import AdvertListAPIView, AdvertDetailAPIView

urlpatterns = [
    path('api/advert-list/', AdvertListAPIView.as_view(), name='advert-list'),
    path('api/advert/<int:pk>/', AdvertDetailAPIView.as_view(), name='advert-detail'),
]
