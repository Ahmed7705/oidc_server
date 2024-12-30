
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.views import callback_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc/', include('oidc_provider.urls', namespace='oidc')),
    path('callback/', callback_view, name='callback'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    


]
