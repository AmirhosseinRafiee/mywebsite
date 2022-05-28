from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=127)
    phone = PhoneNumberField()
    email = models.EmailField()
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "\t".join((self.email, self.title[:20]))