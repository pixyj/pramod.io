from django.shortcuts import render

from blog.models import Post
from home.views import cached_page

ABOUT_ME = """


I'm a full-stack web developer based in Bangalore, India. I love writing beautiful code and
building delightful products. [Here's my resume](https://www.visualcv.com/pramod-lakshmanan).

I also make:

```elixir
Learning
|> Effective
|> Efficient
|> Enjoyable
```

When I'm not programming or improving my CS skills, you'll find me mentoring students, 
playing badminton or basketball, cycling in and around the city, discovering new music and supporting Liverpool.

You can find me on the Internet in these places:

<div class="about-social-links">

* [GitHub](https://github.com/pixyj)

* [Twitter](https://twitter.com/pixyj)

* [Stack Overflow](http://www.stackoverflow.com/users/817277/pramod)

* [Quora](https://www.quora.com/profile/Pramod-Lakshmanan)

</div>


___________

### Trivia

* <span class="about-trivia-item-name">Emacs or Vim:</span> Sublime Text in Vintage mode

* <span class="about-trivia-item-name">Excited About:</span> WebGL, NLP, Elixir

* <span class="about-trivia-item-name">React, Vue or Angular:</span> React, with ES2016/Babel

* <span class="about-trivia-item-name">Django or Rails:</span> Django! These "old" frameworks are still relevant

* <span class="about-trivia-item-name">Heroku or App Engine:</span> Both!

* <span class="about-trivia-item-name">Coding Music:</span> Smooth Jazz, Trance

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.4.0/languages/elixir.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
"""


@cached_page(seconds=3600)
def about(request):
    about_html = Post.md_to_html(ABOUT_ME)
    print(about_html)
    return render(request, "about.html", {"about": about_html})
