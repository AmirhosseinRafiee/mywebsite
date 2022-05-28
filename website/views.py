from django.shortcuts import render
from django.contrib import messages
from .serializers import NewsletterSerializer, ContactSerializer

def index_view(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email')
        }
        ser = NewsletterSerializer(data=data)
        if ser.is_valid():
            ser.save()
            messages.success(request, 'شما عضو خبرنامه شدید.')
        else:
            messages.info(request, 'شما عضو خبرنامه بودید!')
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'email': request.POST.get('email'),
            'title': request.POST.get('title'),
            'message': request.POST.get('message')
        }
        ser = ContactSerializer(data=data)
        if ser.is_valid():
            ser.save()
            messages.success(request, 'پیام شما ثبت شد.')
        else:
            messages.warning(request, 'پیام شما ثبت نشد!')
    return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')
