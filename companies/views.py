from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from .serializers import (
    Company,
    Stock,
    CompanyListSerializer,
    CompanyRetrieveSerializer,
    StockListSerializer,
)


class CompanyListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CompanyRetrieveSerializer
    lookup_field = "id"

    def get_object(self):
        return get_object_or_404(Company, **self.kwargs)


class StockListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Stock.objects.all()
    serializer_class = StockListSerializer
