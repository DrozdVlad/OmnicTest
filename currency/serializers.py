from django.contrib.auth.models import User, Group
from rest_framework import serializers

from currency.models import Currency
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'name', 'rate', 'abbreviation', 'exchange_date']
