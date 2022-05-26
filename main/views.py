from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from main.forms import CommentFormForPost
from main.models import Post, Project


class MainPage(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class ProjectPage(ListView):
    model = Project
    template_name = 'work.html'
    context_object_name = 'projects'


class DetailPost(View):
    template_name = 'detail_post.html'
    comment_form = CommentFormForPost

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post)
        context = {}
        context['post'] = post
        context['comments'] = post.comments.filter(status_comment=True)
        return render(request, template_name=self.template_name, context=context)


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactPage(TemplateView):
    template_name = 'contact.html'
