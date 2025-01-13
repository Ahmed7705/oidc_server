# C:\Users\ahmed\Desktop\SSO Project\SSO\oidc_server\oidc_server\authentication\views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from oidc_provider.admin import ClientForm
from oidc_provider.models import Client
from django.contrib import messages

def callback_view(request):
    return HttpResponse("Callback handled successfully!")


def userinfo(claims, user):
    """
    إعداد بيانات المستخدم التي سيتم إرسالها عند استدعاء /userinfo.
    """
    claims['name'] = user.get_full_name()
    claims['email'] = user.email
    claims['preferred_username'] = user.username
    return claims


def create_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client created successfully!")
            return redirect('client_list')  # استبدل بالمسار المناسب بعد الحفظ
    else:
        form = ClientForm()

    return render(request, 'oidc_provider/create_client.html', {'form': form})

def client_list_view(request):
    clients = Client.objects.all()
    return render(request, 'oidc_provider/client_list.html', {'clients': clients})

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    id_token_hint = request.session.get('id_token')
    
    if not id_token_hint:
        # معالجة حالة عدم وجود id_token
        return redirect('/error/')  # يمكنك توجيه المستخدم إلى صفحة خطأ مناسبة

    post_logout_redirect_uri = 'http://rp.example.com/logged-out/'
    state = 'random_state_value'
    end_session_url = f"http://localhost:8010/oidc/end-session/?id_token_hint={id_token_hint}&post_logout_redirect_uri={post_logout_redirect_uri}&state={state}"
    
    return redirect(end_session_url)
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
import pprint  # مكتبة لطباعة البيانات بشكل منسق

def logout_view(request):
    # طباعة بيانات الطلب
    print("Request Data:")
    pprint.pprint(request.session.__dict__)  # طباعة محتوى الطلب بشكل منسق

    # تنفيذ تسجيل الخروج
    logout(request)
    id_token_hint = request.session.get('id_token')
    
    if not id_token_hint:
        # معالجة حالة عدم وجود id_token
        return redirect('/error/')  # يمكنك توجيه المستخدم إلى صفحة خطأ مناسبة

    post_logout_redirect_uri = 'http://rp.example.com/logged-out/'
    state = 'random_state_value'
    end_session_url = f"http://localhost:8010/oidc/end-session/?id_token_hint={id_token_hint}&post_logout_redirect_uri={post_logout_redirect_uri}&state={state}"
    
    return redirect(end_session_url)
