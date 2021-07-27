import datetime

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import permissions

from currency.models import Currency
from currency.serializers import CurrencySerializer
from currency.utils import collect


class Logout(APIView):
    permission_class = permissions.IsAuthenticatedOrReadOnly

    def get(self, request):
        request.user.auth_token.delete()
        return Response({}, status=status.HTTP_200_OK)


class CurrencyListView(ListAPIView):
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        collect()
        return Currency.objects.all()
