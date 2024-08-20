from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.template import loader
from .forms import NewCommentForm

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    context = {
        "latest_post_list": latest_post_list,
    }
    return render(request, "blog/index.html", context )


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
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
    return render(request, "blog/detail.html", {"post": post, 'comments': user_comment, 'comments': comments, 'comment_form':comment_form} )

    # try:
    #     post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "blog/detail.html", {"post": post})

def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)
