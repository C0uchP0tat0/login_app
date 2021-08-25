from django.contrib import admin
from django.urls import path, include
from login_app.views import accounts, SignUpView

urlpatterns = [
    path ('', accounts, name='accounts'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]
