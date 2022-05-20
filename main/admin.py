from django.contrib import admin

# Register your models here.
from main.models import Developer, Post, Project

admin.site.register(Developer)
admin.site.register(Post)
admin.site.register(Project)
