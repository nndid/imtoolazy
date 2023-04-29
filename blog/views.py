from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Post


class Bloglist(ListView):
    model = Post
    template_name = 'home.html'
    total_posts = Post.objects.count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)   # 10 поумолчанию


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    total_posts = Post.objects.count()


class AboutPageView(TemplateView):
    template_name = 'about.html'
    total_posts = Post.objects.count()


class Razdel1(ListView):
    template_name = 'pozn.html'
    model = Post
    total_posts = Post.objects.count()

    def get_queryset(self):
        object_list = Post.objects.filter(section="Раздел 1")
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)   # 10 поумолчанию


class Razdel2(ListView):
    template_name = 'len.html'
    model = Post
    total_posts = Post.objects.count()

    def get_queryset(self):
        object_list = Post.objects.filter(section="Раздел 2")
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)   # 10 поумолчанию


class Etc(TemplateView):
    template_name = 'etc.html'


class SearchResultView(ListView):
    model = Post
    template_name = "search_result.html"
    total_posts = Post.objects.count()

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query) | Q(author__username__icontains=query)
            ).distinct()
        else:
            object_list = Post.objects.all()
        return object_list
