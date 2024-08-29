import datetime
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.tag_text

class Post(models.Model):
    post_title = models.CharField(max_length=500, default=None)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    post_text = models.TextField(max_length=1000, default=None)
    pub_date = models.DateTimeField(default=timezone.now)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post', default=None)
    thumbsups = models.ManyToManyField(User, related_name='post_thumbsup', default=None, blank=True)
    thumbsdowns = models.ManyToManyField(User, related_name='post_thumbsdown', default=None, blank=True)
    def number_of_thumbsup(self):
        return self.thumbsups.count()
    def number_of_thumbsdown(self):
        return self.thumbsdowns.count()
    def __str__(self):
        return self.post_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments' )
    comment_author_name = models.CharField(max_length=50) 
    comment_author_email = models.EmailField()
    comment_text = models.TextField()
    # comment_author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    comment_published_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("comment_published_date",)

    def __str__(self):
        return f"Comment by {self.comment_author_name}"

class Vote(models.Model):
    post = models.ForeignKey(Post, related_name='postid', on_delete=models.CASCADE, default=None, blank=True)
    user = models.ForeignKey(User, related_name='userid', on_delete=models.CASCADE, default=None, blank=True)
     # ThumbsUp=True, ThumbsDown=False
    vote = models.BooleanField(default=True)
