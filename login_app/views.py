from django.contrib.auth.models import User
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()  # Добавляем в queryset
    serializer_class = UserRegisterSerializer

    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        # Проверка данных на валидность
        if serializer.is_valid():
            # TODO возвращать пользователя
            serializer.save()  # Сохраняем нового пользователя
            return Response(serializer.data['username'], status=status.HTTP_200_OK)  # Возвращаем имя успешно созданого пользователя
        else: 
            data = serializer.errors  # Присваиваем data ошибку
            return Response(data, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибку


class UserViewSet(ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()  # Получаем список пользователей
    serializer_class = UserSerializer
