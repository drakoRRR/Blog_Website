from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.forms import CreatePostForm, UpdatePostForm
from blog.models import Post, Comment
from common.views import CommentFormMixin, SortMixin
from users.forms import CommentForm
from users.models import User


# Create your views here.
class FeedView(SortMixin, CommentFormMixin, ListView):
    model = Post
    template_name = 'blog/feed_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FeedView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/add_post_page.html'
    success_url = reverse_lazy('blog:feed')

    def post(self, request, *args, **kwargs):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog:feed')
        return self.get(request, *args, **kwargs)


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:feed')

    def post(self, request, *args, **kwargs):
        if request.POST.get('action') == 'delete':
            post = get_object_or_404(Post, pk=request.POST.get('post_id'))
            if post.author == request.user:
                post.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)


class ShowPostView(CommentFormMixin, DetailView):
    model = Post
    template_name = 'blog/post_page.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowPostView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/set_post_page.html'
    success_url = reverse_lazy('blog:feed')

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.text_post = self.request.POST['description']
            if self.request.POST['image']:
                post.image = self.request.POST['image']
            form.save()
            return redirect('blog:feed')
        return self.get(request, *args, **kwargs)


class SearchView(CommentFormMixin, ListView):
    model = Post
    template_name = 'blog/search_page.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(text_post__icontains=query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        query = self.request.GET.get('q')
        context['users'] = User.objects.filter(username__icontains=query)
        context['form'] = CommentForm()
        context['search'] = query
        return context

def like_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

