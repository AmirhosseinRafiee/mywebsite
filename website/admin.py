from django.contrib import admin
from .models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('email', 'title', 'created_date')
    list_filter = ('email', 'phone')
    search_fields = ('title', 'message')

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
