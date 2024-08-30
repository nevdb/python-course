from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.template import loader
from .forms import NewCommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Post, Tag

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    context = {
        "latest_post_list": latest_post_list,
    }
    return render(request, "blog/index.html", context )


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    tags = post.tag.all()
    print(tags)
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/')
    else:
        comment_form = NewCommentForm()
    return render(request, "blog/detail.html", {"post": post, 'comments': user_comment, 'comments': comments, 'tags': tags, 'comment_form':comment_form} )

@login_required
def post_thumbsup(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.thumbsups.filter(id=request.user.id):
        post.thumbsups.remove(request.user)
    else:
        post.thumbsups.add(request.user)

    return render(request,'blog/detail.html', {"post": post} )

@login_required
def post_thumbsdown(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.thumbsdowns.filter(id=request.user.id):
        post.thumbsdowns.remove(request.user)
    else:
        post.thumbsdowns.add(request.user)

    return render(request,'blog/detail.html', {"post": post} )

class TagListView(ListView):
    template_name = 'blog/tag.html'
    context_object_name = 'taglist'

    def get_queryset(self):
        content = {
            'tag': self.kwargs['tag'],
            'posts': Post.objects.filter(tag__title=self.kwargs['tag'])
        } 
        return content
    
def tag_list(request):
    tag_list = Tag.objects.all()
    context = {
        "tag_list": tag_list,
    }
    return context