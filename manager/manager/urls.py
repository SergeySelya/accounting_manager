from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

router.register(r"categories", views.CategoryModelViewSet, basename="category")
router.register(r"transactions", views.TransactionModelViewSet, basename="transaction")
# router.register(r"currencies", views.CurrencyModelViewSet, basename="currency")
# статистика баланс
# router.register(r"statistics", views.StatisticListAPIViewModelViewSet, basename="statistic")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", obtain_auth_token, name="obtain-auth-token"),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
] + router.urls



