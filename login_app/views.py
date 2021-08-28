from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .serializers import UserSerializer, UserRegistrSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()  # Добавляем в queryset
    serializer_class = UserRegistrSerializer
    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        # Проверка данных на валидность
        if serializer.is_valid():
            serializer.save() # Сохраняем нового пользователя
            data['response'] = True # Добавляем в список значение ответа True
            return Response(data, status=status.HTTP_200_OK) # Возвращаем что всё в порядке
        else: 
            data = serializer.errors # Присваиваем data ошибку
            return Response(data) # Возвращаем ошибку

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    #permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

@api_view(['GET'])
def api_accounts(request):
    if request.method == 'GET':
        accounts = User.objects.all()
        serializer = UserSerializer(accounts, many=True)
        return Response(serializer.data)


@login_required(login_url='/accounts/login/')
def accounts(request):
    users = User.objects.all()
    context = {'users': users,}
    return render(request, 'accounts.html', context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
