import datetime
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    post_title = models.CharField(max_length=500, default=None)
    post_text = models.TextField(max_length=1000, default=None)
    pub_date = models.DateTimeField(default=timezone.now)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post', default=None)
    def __str__(self):
        return self.post_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Tag(models.Model):
    post = models.ManyToManyField(Post, default=None)
    tag_text = models.CharField(max_length=100)
    pass

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
    post = models.ManyToManyField(Post, default=None)
     # ThumbsUp=True, ThumbsDown=False
    vote = models.BooleanField(default=True)
