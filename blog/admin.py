from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    exclude = ('counted_view',)
    list_display = ('title', 'author', 'status', 'counted_view', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ('title',)
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    exclude = ('created_date',)
    list_display = ('name', 'email', 'approved', 'title', 'created_date')
    list_filter = ('email', 'approved')
    search_fields = ('title', 'message')

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
