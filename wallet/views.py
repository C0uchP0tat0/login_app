from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from login_app.serializers import UserSerializer, WalletSerializer
from .models import Wallet


class UserWallet(APIView):

    def get_object(self, pk): # получаем кошелёк пользователя по id кошелька
        try:
            return Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_wallet = self.get_object(pk)
        serializer = WalletSerializer(user_wallet)
        return Response(serializer.data)

    def put(self, request, pk, format=None): # пополняем выбранный кошелёк
        user_wallet = self.get_object(pk)
        serializer = WalletSerializer(user_wallet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   