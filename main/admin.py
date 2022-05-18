from django.contrib import admin

# Register your models here.
from main.models import Developer, Post

admin.site.register(Developer)
admin.site.register(Post)