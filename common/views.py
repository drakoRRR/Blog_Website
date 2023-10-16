from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from blog.models import Post, Comment
from users.forms import CommentForm


class CommentFormMixin:
    def post(self, request, *args, **kwargs):
        if request.POST.get('action') == 'delete':
            return self.delete_comment(request, *args, **kwargs)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=kwargs['post_id'])
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)

    def delete_comment(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
        if comment.post.author == request.user or comment.author == request.user:
            comment.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)


