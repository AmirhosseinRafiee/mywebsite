from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Comment
from .serializers import Commentserializer

def index_view(request, author_username=None, cat_name=None, tag_name=None):
    posts = Post.objects.filter(status=1)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if cat_name:
        posts = posts.filter(categories__name=cat_name)
    if tag_name:
        posts = posts.filter(tags__name=tag_name)
    paginator = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page', 1)
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def single_view(request, pid):
    if request.method == 'POST':
        data = {
            'post': pid,
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'title': request.POST.get('title'),
            'message': request.POST.get('message')
        }
        ser = Commentserializer(data=data)
        if ser.is_valid():
            ser.save()
            messages.success(request, 'نظر شما ثبت شد')
        else:
            messages.error(request, 'نظر شما ثبت نشد!')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()
    comments = Comment.objects.filter(post=post, approved=1)
    try:
        next_post = posts.filter(id__gt=pid).order_by('id')[0]        
    except:
        next_post = None     
    try:
        prev_post = posts.filter(id__lt=pid).order_by('-id')[0]
    except:
        prev_post = None
    context = {'post': post, 'comments': comments, 'next_post': next_post, 'prev_post': prev_post}
    return render(request, 'single-post.html', context)