from django.shortcuts import render

from blog.models import Post
from home.views import cached_page

ABOUT_ME = """
I'm a web developer based in Bangalore, India. I love writing beautiful code and
building delightful products. [Here's my resume](https://www.visualcv.com/pramod-lakshmanan).

I'm particularly passionate about making the process of learning more efficient
and enjoyable through software and my side-projects are usually educational apps.


When I'm not coding or improving my CS and programming skills, you'll find me mentoring students, 
playing basketball, cycling in and around the city, discovering new music or supporting Liverpool.


You can find me on the Internet in these places:

[GitHub](https://github.com/pixyj)

[Twitter](https://twitter.com/pixyj)

[Stack Overflow](http://www.stackoverflow.com/users/817277/pramod)

[Quora](https://www.quora.com/profile/Pramod-Lakshmanan)

________

**Trivia**

*Emacs or Vim:* Sublime Text in Vintage mode

*React or Angular:* React, with ES6

*Rails or Django:* Django. These "old" frameworks are still relevant.

*Heroku or App Engine:* Both!
"""


@cached_page(seconds=3600)
def about(request):
    about_html = Post.md_to_html(ABOUT_ME)
    print(about_html)
    return render(request, "about.html", {"about": about_html})
