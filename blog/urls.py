from django.urls import path
from django.views.generic import ListView
from .views import BlogList, BlogDetailView, AboutPageView

urlpatterns = [
    path('', BlogList.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
]
