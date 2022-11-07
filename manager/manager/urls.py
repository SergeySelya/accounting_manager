from django.contrib import admin
from django.urls import path, include, re_path
from core import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

router.register(r"categories", views.CategoryModelViewSet, basename="category")
router.register(r"transactions", views.TransactionModelViewSet, basename="transaction")
# статистика баланс
router.register(r"statistics", views.StatisticListAPIView, basename="statistic")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('djoser.urls')),
    re_path(r"^auth/", include('djoser.urls.authtoken')),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
    path("report/", views.TransactionReportAPIView.as_view(), name="report"),

] + router.urls



