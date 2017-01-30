from django.contrib.syndication.views import Feed
from blog.models import Post


class PostsFeed(Feed):
    title = "Pramod's blog"
    link = "/blog/"
    description = "The latest posts from Pramod's blog"

    def items(self):
        return Post.objects.order_by("-created").filter(is_published=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html_content

    def item_link(self, item):
        return item.url
