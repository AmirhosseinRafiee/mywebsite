from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from jalali_date import date2jalali

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(max_length=511)
    content = models.TextField()
    counted_view = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    # comments
    categories = models.ManyToManyField(Category)
    tags = TaggableManager()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-published_date',)

    def get_jalali_date(self):
        return date2jalali(self.published_date)

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    title = models.CharField(max_length=510)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_date',)

    def get_jalali_date(self):
        return date2jalali(self.created_date)

    def __str__(self):
        return 'Comment {} by {}'.format(self.title, self.email)