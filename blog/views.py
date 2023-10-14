from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class FeedView(TemplateView):
    template_name = 'blog/feed_page.html'
