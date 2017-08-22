from django.db import models

from blog.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField()
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    @property
    def html_description(self):
        return Post.md_to_html(self.description)

    def __str__(self):
        return "{} {} - {}".format(self.name,
                                   self.start_date,
                                   self.end_date)
