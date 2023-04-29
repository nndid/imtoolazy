from django.urls import path


from .views import Bloglist, BlogDetailView, AboutPageView, Razdel1, Razdel2, Etc, SearchResultView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
    path('pozn/', Razdel1.as_view(), name='pozn'),
    path('len/', Razdel2.as_view(), name='len'),
    path('etc/', Etc.as_view(), name='etc'),
    path('search/', SearchResultView.as_view(), name='search_results')
]