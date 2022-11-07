from datetime import datetime

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from post_office import mail
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Category, Currency, Transaction
from core.reports import transaction_report
from core.serializers import (CategorySerializer, CurrencySerializer,
                              ReadTransactionSerializer, ReportEntrySerializer,
                              ReportParamsSerializer,
                              StatisticTransactionSerializer,
                              WriteTransactionSerializer)

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


class TransactionReportAPIView(APIView):
    def get(self, request):
        params_serializer = ReportParamsSerializer(data=request.GET, context={"request": request})
        params_serializer.is_valid(raise_exception=True)
        params = params_serializer.save()
        data = transaction_report(params)
        serializer = ReportEntrySerializer(instance=data, many=True)
        return Response(data=serializer.data)


class Sendmail():
    a = User.objects.all()
    for el in a:
        info = Transaction.objects.all().filter(user_id=el.id, date__contains=datetime.today().date())
        if info:
            mail.send(
                'elhom99@gmail.com',
                subject='Transaction from yestarday',
                message=f'{info}',
            )
