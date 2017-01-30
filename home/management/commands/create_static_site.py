import os
import requests
from django.core.management.base import BaseCommand

from blog.models import Post


class Command(BaseCommand):

    def _create_output_dir(self, output_dir):
        try:
            os.mkdir(output_dir)
        except FileExistsError:
            print("WARN: output dir exists already. Recreating it")
            os.system('rm -r {}'.format(output_dir))
            os.mkdir(output_dir)

    def _url_to_file(self, url, file_path):
        response = requests.get(url)
        html_binary_string = response.content
        with open(file_path, "wb") as f:
            f.write(html_binary_string)

    def handle(self, *args, **options):
        root_dir = "helloworld/static_site"
        host = "http://localhost:4444"
        self._create_output_dir(root_dir)

        # home
        self._url_to_file(host, "{}/index.html"
                          .format(root_dir))

        # about
        self._url_to_file("{}/about/".format(host), "{}/about.html".
                          format(root_dir))

        # contact
        self._url_to_file("{}/contact/".format(host),
                          "{}/contact.html".format(root_dir))

        # css
        self._create_output_dir("{}/static".format(root_dir))
        files = ['material.css', 'styles.css', 'per.css',
                 'per.html', 'per.js', 'p.png']
        for f in files:
            self._url_to_file("{}/static/{}/".format(host, f),
                              "{}/static/{}".format(root_dir, f))

        # blog home
        self._url_to_file("{}/blog/".format(host),
                          "{}/blog.html".format(root_dir))

        # blog posts
        Post.collect_published_posts("{}/blog".format(root_dir))

        # rss
        self._url_to_file("{}/rss/".format(host),
                          "{}/rss.xml".format(root_dir))
        self._url_to_file("{}/static/{}/".format(host, 'feed-icon.svg'),
                          "{}/static/{}".format(root_dir, 'feed-icon.svg'))
