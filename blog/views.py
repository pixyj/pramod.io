from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post


def get_blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.is_not_published:
        raise Http404
    return render(request, "post.html", {"post": post})
