import os
import subprocess
from django.db import models
from django.utils.text import slugify

import requests


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    slug = models.CharField(unique=True, editable=False, max_length=256)
    markdown_content = models.TextField()
    is_published = models.BooleanField(default=False)

    # Property Methods
    @property
    def is_not_published(self):
        """
        Convienience method to check if blog is not published
        """
        return not self.is_published

    @property
    def html_content(self):
        """
        Blog post content is written in markdown.
        So get the HTML version of the content by calling a node command
        which uses the `Remarkable` js library to convert md to html
        """
        # setup
        md_file_path = "/tmp/{}.md".format(self.slug)
        html_file_path = "/tmp/{}.html".format(self.slug)
        with open(md_file_path, 'w') as f:
            f.write(self.markdown_content)

        # Call node command
        command = "node md-to-html.js {} {}"\
                  .format(md_file_path, html_file_path)
        subprocess.check_output(command, shell=True).strip()
        with open(html_file_path, 'r') as f:
            output = f.read().strip()
        exit_code = os.system("rm {}; rm {}".format(
                              md_file_path, html_file_path))
        assert exit_code == 0
        return output

    @property
    def url(self):
        """
        Get blog post url
        """
        return "/blog/{}".format(self.slug)

    # Other public instance methods
    def save(self, *args, **kwargs):
        """
        Override save to create slug
        """
        self.slug = slugify(self.title)
        models.Model.save(self, *args, **kwargs)

    def __str__(self):
        """
        Get the readable string displayed on Admin
        """
        return "{} - Created on {}".format(self.title, self.created)

    # Class methods
    @classmethod
    def _create_output_dir(self, output_dir):
        try:
            os.mkdir(output_dir)
        except FileExistsError:
            print("WARN: output dir exists already. Recreating it")
            os.system('rm -r {}'.format(output_dir))

    @classmethod
    def collect_published_posts(Post, output_dir):
        """
        Save all published posts as HTML files in `output_dir`
        """
        Post._create_output_dir(output_dir)

        published_posts = Post.objects.filter(is_published=True)
        slug_and_urls = [(post.slug, post.url, ) for post in published_posts]

        for slug, url in slug_and_urls:
            full_url = "http://localhost:8000{}".format(url)
            response = requests.get(full_url)
            html_binary_string = response.content
            html_file_path = "{}/{}.html".format(output_dir, slug)
            with open(html_file_path, "wb") as f:
                f.write(html_binary_string)
