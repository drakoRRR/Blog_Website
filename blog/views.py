from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from blog.models import Post


# Create your views here.
class FeedView(ListView):
    model = Post
    template_name = 'blog/feed_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FeedView, self).get_context_data(**kwargs)
        return context


def like_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))