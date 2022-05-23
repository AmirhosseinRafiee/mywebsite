from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:pid>', views.single_view, name='single'),
    path('author/<str:author_username>', views.index_view, name='author'),
    path('category/<str:cat_name>', views.index_view, name='category'),
    path('tag/<str:tag_name>', views.index_view, name='tag'),
]