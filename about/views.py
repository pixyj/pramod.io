from django.shortcuts import render

from blog.models import Post
from home.views import cached_page

ABOUT_ME = """
I'm a web developer based in Bangalore, India. I love writing beautiful code and
building delightful products.

I'm particularly passionate about making the process of learning more efficient
and enjoyable through software and my side-projects are usually educational apps.


When I'm not coding or improving my CS and programming skills, you'll find me mentoring students, 
playing basketball, cycling in and around the city, discovering new music or supporting Liverpool.

You can find me on the interwebs in these places:

[GitHub](https://github.com/pixyj)

[Twitter](https://twitter.com/pixyj)

[Stack Overflow](http://www.stackoverflow.com/users/817277/pramod)

[Quora](https://www.quora.com/profile/Pramod-Lakshmanan)

"""


@cached_page(seconds=3600)
def about(request):
    about_html = Post.md_to_html(ABOUT_ME)
    print(about_html)
    return render(request, "about.html", {"about": about_html})
