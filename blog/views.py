from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Post


class Bloglist(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)  # 10 поумолчанию


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class Razdel1(ListView):
    template_name = 'pozn.html'
    model = Post

    def get_queryset(self):
        object_list = Post.objects.filter(section="Раздел 1")
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)  # 10 поумолчанию


class Razdel2(ListView):
    template_name = 'len.html'
    model = Post

    def get_queryset(self):
        object_list = Post.objects.filter(section="Раздел 2")
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)  # 10 поумолчанию


class Etc(TemplateView):
    template_name = 'etc.html'


class SearchResultView(ListView):
    model = Post
    template_name = "search_result.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query) | Q(author__username__icontains=query)
            ).distinct()
        else:
            object_list = Post.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context


class SignUpView(ListView):
    model = User
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect('signin')


class SignInView(ListView):
    model = Post
    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('home')
        else:
            messages.error(self.request, "wrong username/password")
            return redirect('home')


class UserProfileView(View):
    @staticmethod
    def get(request, user_id):
        user = get_object_or_404(User, pk=user_id)
        posts = user.post_set.all()
        context = {'user': user, 'posts': posts, 'last_login': user.last_login}
        return render(request, 'user_profile.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'logout.html', {})
