from django.contrib import admin
from django.urls import path

from companies import views as companies_views

urlpatterns = [
    path(
        "companies/<int:id>/",
        companies_views.CompanyRetrieveAPIView.as_view(),
        name="retrieve_company",
    ),
    path("companies/", companies_views.CompanyListAPIView.as_view(), name="companies"),
    path("stocks/", companies_views.StockListAPIView.as_view(), name="stocks"),
]
