from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index_view),
    path('contact', views.contact_view),
    path('services', views.services_view),
]
