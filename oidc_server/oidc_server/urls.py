
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.views import callback_view
from authentication import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc/', include('oidc_provider.urls', namespace='oidc')),
    path('callback/', callback_view, name='callback'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('oidc/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('create-client/', views.create_client_view, name='create_client'),
    path('client_list/', views.client_list_view, name='client_list'),





]
