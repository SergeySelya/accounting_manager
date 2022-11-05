from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"categories", views.CategoryModelViewSet, basename="category")
router.register(r"transactions", views.TransactionModelViewSet, basename="transaction")
# router.register(r"currencies", views.CurrencyModelViewSet, basename="currency")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies'),
] + router.urls



