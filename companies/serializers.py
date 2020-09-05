from rest_framework import serializers

from .models import Contact, Company, Stock, Place


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("contact", "is_phone")


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name", "avatar")


class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        exclude = ("places",)


class PlaceSerializer(serializers.ModelSerializer):
    stocks = StockListSerializer(many=True, read_only=True)
    contact_set = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        exclude = ("company",)


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ("places",)
