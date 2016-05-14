from django.shortcuts import render
from django.conf import settings


def cached_page(seconds=600):
    """
    Decorator to cache page for x seconds:
    @cached_page(seconds=100)
    def my_view(request, *args, **kwargs):
        pass
    """
    def outer_wrapper(fn):
        def wrapper(request, *args, **kwargs):
            response = fn(request, *args, **kwargs)
            if settings.CACHE_PAGES is True:
                response.set_cookie("Cache-Control",
                                    "max-age={}".format(seconds))
            return response
        return wrapper
    return outer_wrapper


def home(request):
    """
    Home, sweet home.
    """
    return render(request, "home.html")


