from rest_framework import serializers 
from django.contrib.auth.models import User
from wallet.models import Wallet


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

class WalletSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    balance = serializers.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        model = Wallet
        fields = ['user', 'balance']

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(username=self.validated_data['username'],) # Назначаем Логин
        password = self.validated_data['password'] # Проверяем на валидность пароль
        password2 = self.validated_data['password2'] # Проверяем на валидность повторный пароль
        # Проверяем совпадают ли пароли
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user
