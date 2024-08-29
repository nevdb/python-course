from django.contrib import admin
from .import models
from .models import Post
from .models import Comment

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'pub_date', 'post_author')

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "comment_text", "comment_author_name", "comment_author_email", "comment_published_date")
    # list_filter = ("comment_published_date")

class LeadershipAdmin(AuthorAdmin, CommentAdmin):
    pass
