from django.contrib.auth.models import User
from core.models import Currency, Category,Transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CurrencySerializer, CategorySerializer,ReadTransactionSerializer,WriteTransactionSerializer,StatisticTransactionSerializer
from rest_framework.viewsets import ModelViewSet

#custom return statictic of user
class StatisticListAPIView(ModelViewSet):
    serializer_class = StatisticTransactionSerializer
    queryset = Transaction.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = {}

    def list(self, request, *args, **kwargs):
        a = Transaction.objects.filter(user=self.request.user)
        for el in a:
            if el.currency.code not in self.c.keys():
                self.c[el.currency.code] = int(el.amount)
            else:
                self.c[el.currency.code] += int(el.amount)
        return Response({"statistic": self.c})





class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None



class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TransactionModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,OrderingFilter,DjangoFilterBackend)
    search_fields = ("description",)
    filterset_fields = ("currency__code",)
    # sort from date and amount
    ordering_fields = ("amount", "date")

    def get_queryset(self):
        return Transaction.objects.select_related("currency", "category", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer








