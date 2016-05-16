from django.shortcuts import render

from blog.models import Post
from .models import Project


HEADING = """### Welcome! I'm Pramod Lakshmanan. Here are some of my recent projects."""


def projects(request):
    """
    1. Convert the markdown strings on the top of the page to html
    2. Render the response
    """
    heading_html = Post.md_to_html(HEADING)
    projects = Project.objects.filter(is_published=True).order_by('-created')
    return render(request, 'projects.html', {
        "heading": heading_html,
        "projects": projects
    })
