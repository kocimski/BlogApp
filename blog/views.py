from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    postsbase = Post.objects.all()
    return render(request, "index.html", {'postshtml': postsbase})#pozwala korzystać z post w html

def post(request, slug):
    print(slug)
    posts = Post.objects.all()
    return render(request, "post.html", {
        'post': get_object_or_404(Post, slug = slug),
        'postshtml2' : posts
    })

def about(request):
    return render(request, 'about.html', {})