import webapp2

STATIC_SITE_PATH = "static_site"


def file_path_to_string(path):
    with open("{}/{}".format(STATIC_SITE_PATH, path), 'r') as f:
        s = f.read()
    return s

to_str = file_path_to_string


def cache_page(response):
    response.headers['Cache-Control'] = "max-age=600"
    return response


class Main(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        cache_page(self.response)
        self.response.write(to_str('index.html'))


class Styles(webapp2.RequestHandler):
    def get(self, file_name):
        extension = file_name.split(".")[1]
        content_type = 'text/{}'.format(extension)
        self.response.headers['Content-Type'] = content_type
        cache_page(self.response)
        self.response.write(to_str('static/{}'.format(file_name)))


class About(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        cache_page(self.response)
        self.response.write(to_str('about.html'))


class Contact(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        cache_page(self.response)
        self.response.write(to_str('contact.html'))


class BlogHome(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        cache_page(self.response)
        self.response.write(to_str('blog.html'))


class BlogPost(webapp2.RequestHandler):
    def get(self, slug):
        self.response.headers['Content-Type'] = 'text/html'
        cache_page(self.response)
        self.response.write(to_str('blog/{}.html'.format(slug)))


class RSS(webapp2.RequestHandler):
    def get(self, slug):
        self.response.headers['Content-Type'] = 'application/rss+xml'
        cache_page(self.response)
        self.response.write(to_str('rss.xml'))


app = webapp2.WSGIApplication([
    ('/', Main),
    ('/static/([\w\d\-\.]+)', Styles),
    ('/about/', About),
    ('/contact/', Contact),
    ('/blog/([\w\d\-]+)/', BlogPost),
    ('/blog/', BlogHome),
    ('/rss/', RSS),
], debug=True)
