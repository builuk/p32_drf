from django.contrib import admin
from posts.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at")

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "text", "created_at")