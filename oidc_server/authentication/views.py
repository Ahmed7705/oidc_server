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
