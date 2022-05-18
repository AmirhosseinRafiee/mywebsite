from django.shortcuts import render

def index_view(request):
    return render(request, 'blog.html')

def single_view(request):
    return render(request, 'single-post.html')