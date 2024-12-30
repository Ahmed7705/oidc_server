from django.http import HttpResponse

def callback_view(request):
    return HttpResponse("Callback handled successfully!")
