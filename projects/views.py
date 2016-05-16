from django.shortcuts import render

from blog.models import Post

# Create your views here.


HEADING = """
## HEADING
"""


COASTER = """
## COASTER
"""

REPORTS = """
## REPORTS
"""

PROJECTS = [COASTER, REPORTS]


def projects(request):
    """
    1. Convert the markdown strings on the top of the page to html
    2. Render the response
    """
    heading_html = Post.md_to_html(HEADING)
    projects_html = [Post.md_to_html(p) for p in PROJECTS]
    return render(request, 'projects.html', {
        "heading": heading_html,
        "projects": projects_html
    })
