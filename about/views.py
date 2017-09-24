from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post
from home.views import cached_page

ABOUT_ME = """


I'm a full-stack web developer based in Bangalore, India. I love writing beautiful code to
build delightful products. [Here's my resume](https://stackoverflow.com/users/story/817277?view=Cv).

I also make:

```elixir
Learning
 ▶ Effective
 ▶ Efficient
 ▶ Enjoyable
```
___________

When I'm not programming or improving my CS skills, you'll find me 

* Mentoring students
* Playing badminton or basketball with my best mates.
* Cycling in and around the city
* Discovering new music
* Supporting Liverpool.


__________

You can find me on the Internet in these places:

<div class="about-social-links">

<span><img src="/static/icons/github.png" class="social-icon alt="GitHub"" />[pixyj](https://github.com/pixyj)</span>

<span><img src="/static/icons/twitter.png" class="social-icon alt="Twitter" />[pixyj](https://twitter.com/pixyj)</span>

<span><img src="/static/icons/stackoverflow.ico" class="social-icon alt="StackOverflow" />[Pramod](http://www.stackoverflow.com/users/817277/pramod)</span>

<span><img src="/static/icons/hn.ico" class="social-icon" alt="HN"/>[pramodliv1](https://news.ycombinator.com/user?id=pramodliv1)</span>


<span><img src="/static/icons/quora.png" class="social-icon" alt="Quora" />[Pramod Lakshmanan](quora.com/pramod-lakshmanan)</span>


</div>


___________

### Trivia

* <span class="about-trivia-item-name">Emacs or Vim:</span> Sublime Text 3 in Vintage mode. (Yes I finally paid the license!)

* <span class="about-trivia-item-name">Excited About:</span> WebGL, NLP, Elixir, CoffeeScript 2.0

* <span class="about-trivia-item-name">React, Vue or Angular:</span> React, with ES2015/Babel. (I do miss my first love, `Backbone.js`)

* <span class="about-trivia-item-name">Django or Rails:</span> Django! These "old" frameworks are still relevant.

* <span class="about-trivia-item-name">Heroku or App Engine:</span> Both! But for different use cases.

* <span class="about-trivia-item-name">Coding Music:</span> Smooth Jazz, Trance, Relaxing music on YouTube

* <span class="about-trivia-item-name">Tabs or Spaces:</span> 4 Spaces for Python, 2 spaces for JS and Elixir

* <span class="about-trivia-item-name">SQL Or NoSQL</span> v1. SQL + Redis; v2. NoSQL if necessary.

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.4.0/languages/elixir.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
"""

KEYBASE_TXT = """
==================================================================
https://keybase.io/pixyj
--------------------------------------------------------------------

I hereby claim:

  * I am an admin of https://pramod.io
  * I am pixyj (https://keybase.io/pixyj) on keybase.
  * I have a public key with fingerprint 8D6D 422D 5213 FBBA 29A7  B0A6 64B8 E4D3 338B E6AF

To do so, I am signing this object:

{
  "body": {
    "key": {
      "eldest_kid": "0101bcfdf14500e16771eed54fa435d77d2a378a1551964df822f03f97d49ae1f1940a",
      "fingerprint": "8d6d422d5213fbba29a7b0a664b8e4d3338be6af",
      "host": "keybase.io",
      "key_id": "64b8e4d3338be6af",
      "kid": "0101bcfdf14500e16771eed54fa435d77d2a378a1551964df822f03f97d49ae1f1940a",
      "uid": "42bb545522afcf59d755c6c7d9a1b619",
      "username": "pixyj"
    },
    "service": {
      "hostname": "pramod.io",
      "protocol": "https:"
    },
    "type": "web_service_binding",
    "version": 1
  },
  "ctime": 1506200694,
  "expire_in": 157680000,
  "prev": "259bd125abb496cf8645b19bf7d1fac66ae868197378e45d5c44a07b3d59fa7e",
  "seqno": 5,
  "tag": "signature"
}

which yields the signature:

-----BEGIN PGP MESSAGE-----
Version: Keybase OpenPGP v2.0.73
Comment: https://keybase.io/crypto

yMIrAnicrVJbSFRBGF7LrLaLS0Rk+uLpRXCpM2dn5pyzUVlGD/ZQ0Q2h2GbOzNhR
27OdXTc3zcBKH8zSyCjQLhJ2oaD7FSoriuhKBEKl3cykDI3C0nroHKu3HpuXYb75
vu///p//1rjhHm/SxLxFJZVnc64k3WutL/Hk374fL5OoxRJSsEwq4kMXL2Y8GgsV
mUwKSjKQATUEEwAiWeYAqyrgnCEoCAwgpqpMIQFVIwAhoGPIhKYoQg4IXWVQJxwI
oEOZSH5JmOECbkdsMxxzbDWGGVQUhhQQEJQSRScqlQnGkGocskAgoFGOiXCEa6yo
q3DCURLl00zLwZxHaCjeP/j/OXfJkB1UKEUQIUUhwhBIZypCBjZUphNAMdBdYpTb
YbKWO+yIWZoolDb6JQeKmwZ3p+q28ffbJmst9ruTiG3FLMMqduA1sVgkGnRlsUTE
5a3nNPTHIUTNMHMm6Cji3I6aVlgKAodpxEzXEiAZK7KMdeiXeGnEtHnIdBlIxZrs
HLcOjzuWCtIpAwoilEIdG0LDEFGgU6EyIIiBMeEa1oCuOrPhEDFkQEhklQYY0gVR
ueT2tC5sSUHkxCQFjmXULAiTWInNpY03rq9M9iR5PSkjhrmb5fGO9v3dt4asUZ79
t3ozjvVvHejxnZ70Ijd94PHgtxPnRuauXvZl/NFhvu83G5oWVhhn7uW83PHTe9qf
P6Zjed8b3wpfeyFeHDrSWHs1nj2zrn6l3F3kO3tKruquadmkbFnduK/jwo+WWaQ1
cv1VdXnx/T3RnW/fP2//+SmzovOSN7Xy8tLC410pU5v73mb2ds/7cDildcyXvFVp
o2c/m3ENp56bf+j1xcoFaeUf2877l9zpvTAlte3b7kvNJx+Xaf1dlxPpaFl18vRN
YkTBg6aqh6c6c7ZNvvakJrsne3KLfnBz1vyn67UNgzVjH8225/TdpbVLrwYPzCva
e2bCu+Smrxm72sqaSz/X7Z5yN3EUzW3b/gtz10Z2
=/Zmy
-----END PGP MESSAGE-----

And finally, I am proving ownership of this host by posting or
appending to this document.

View my publicly-auditable identity here: https://keybase.io/pixyj

==================================================================
"""


@cached_page(seconds=3600)
def about(request):
    about_html = Post.md_to_html(ABOUT_ME)
    print(about_html)
    return render(request, "about.html", {"about": about_html})


@cached_page(seconds=3600)
def keybase(request):
    return HttpResponse(KEYBASE_TXT, content_type='text/plain')

