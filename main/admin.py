from django.contrib import admin

# Register your models here.
from main.models import Developer, Post, Project, CommentForPost

admin.site.register(Developer)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(CommentForPost)
