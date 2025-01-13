# C:\Users\ahmed\Desktop\SSO Project\SSO\oidc_server\oidc_server\oidc_server\urls.pyC:\Users\ahmed\Desktop\SSO Project\SSO\oidc_server\oidc_server\oidc_server\urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.views import callback_view
from authentication import views
from oidc_provider import views as oidc_views
from authentication.views import logout_view





urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc/', include('oidc_provider.urls', namespace='oidc')),
    path('callback/', callback_view, name='callback'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('oidc/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('create-client/', views.create_client_view, name='create_client'),
    path('client_list/', views.client_list_view, name='client_list'),
    path('oidc/end-session/', oidc_views.EndSessionView.as_view(), name='end-session'),
    path('logout/', logout_view, name='logout'),



]
