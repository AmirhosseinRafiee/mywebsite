from django import template
from blog.models import Category, Post, Comment

register = template.Library()

@register.filter
def snippet(value, arg=200):
    return '{}...'.format(value[:arg])

@register.simple_tag
def comments_count(pid):
    comments_count = Comment.objects.filter(post=pid,approved=1).count()
    return comments_count

@register.simple_tag
def latestposts_home(f, t):
    posts = Post.objects.filter(status=1)[f:t]
    return posts  

@register.inclusion_tag('blog-categories.html')
def categories():
    categories = Category.objects.all()
    return {'categories': categories}

@register.inclusion_tag('blog-latestposts.html')
def latestposts(arg=3):
    latestposts = Post.objects.filter(status=1)[:arg]
    return {'latestposts': latestposts}

@register.inclusion_tag('blog-tags.html')
def tags():
    tags = Post.tags.most_common()[:15]
    return {'tags': tags}

