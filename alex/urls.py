from django.contrib import admin
from django.urls import path, include
from login_app.views import api_accounts, RegistrUserView, UserDetailView, home

urlpatterns = [
    path ('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('api/signup/', RegistrUserView.as_view(), name='registr'),
    path('api/accounts/', api_accounts, name='accounts'),
    path('api/accounts/<int:pk>', UserDetailView.as_view(), name="my"),
]
