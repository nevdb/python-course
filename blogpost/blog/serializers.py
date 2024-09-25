from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Tag, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

# ???
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ['title', 'id']
        read_only_fields = ['id']


class PostSerializer(serializers.ModelSerializer):
   tags = TagSerializer(many=True, read_only=True)
   owner = serializers.ReadOnlyField(source='owner.username')

   class Meta:
       model = Post
       fields = ['id', 'tags', 'post_title', 'post_text', 'pub_date', 'post_author', 'owner', 'thumbsups', 'thumbsdowns' ]
       read_only_fields = ['id', 'post_author', 'owner', 'tag' ]

class CommentSerialization(serializers.ModelSerializer):
    post = PostSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'comment_author_name', 'comment_author_email', 'comment_published_date ']


