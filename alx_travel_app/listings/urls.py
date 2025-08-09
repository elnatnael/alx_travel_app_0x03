from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import initiate_payment, verify_payment

urlpatterns = [
    path('payment/initiate/', initiate_payment, name='initiate-payment'),
    path('payment/verify/<str:tx_ref>/', verify_payment, name='verify-payment'),
]