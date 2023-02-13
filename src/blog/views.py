from django.shortcuts import render, redirect

from blog.models import BlogPost


def home(request):
    return redirect('post_index')


def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


# Create your views here.
def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'post': post})
