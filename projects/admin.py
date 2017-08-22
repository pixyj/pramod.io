from django.contrib import admin
from .models import Project, Tag


admin.site.register(Tag)
admin.site.register(Project)
