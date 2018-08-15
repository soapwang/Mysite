from django.urls import path, re_path
from . import views
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^home/', views.index, name='index'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^blog/$', ListView.as_view(
    queryset=Post.objects.all().order_by("-date"), template_name="blog/blog.html")),
    # ?P means named group, pk stands for primary key
    re_path(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post,
    template_name= 'blog/post.html')),
    re_path(r'^signin/$', views.signin, name='signin'),
    re_path(r'^signin/signin_auth/', views.signin_auth, name='signin_auth'),
]
