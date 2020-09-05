from django.contrib import admin

from .models import Contact, Company, Stock, Place


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Contact._meta.fields]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Stock._meta.fields]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Place._meta.fields]
