from django.contrib import admin
from django.urls import path, include
from login_app.views import accounts, SignUpView, api_accounts, RegistrUserView, UserDetailView

urlpatterns = [
    path ('', accounts, name='accounts'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('api/accounts/', api_accounts, name='api_accounts'),
    path('api/signup/', RegistrUserView.as_view(), name='registr'),
    path('api/accounts/<int:pk>',UserDetailView.as_view(),name="my_account"),
]
