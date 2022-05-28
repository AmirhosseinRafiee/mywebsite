from rest_framework import serializers
from .models import Newsletter, Contact

class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact 
        fields = '__all__'