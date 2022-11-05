from django.shortcuts import render
from core.models import Currency, Category,Transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from .serializers import CurrencySerializer, CategorySerializer,ReadTransactionSerializer,WriteTransactionSerializer
from rest_framework.viewsets import ModelViewSet


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.select_related("currency", "category")
    filter_backends = (SearchFilter,OrderingFilter,DjangoFilterBackend)
    search_fields = ("description",)
    filterset_fields = ("currency__code",)
    # sort from date and amount
    ordering_fields = ("amount", "date")


    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer



