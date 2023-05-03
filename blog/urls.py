from django.urls import path

from . import views
from .views import Bloglist, BlogDetailView, AboutPageView, Razdel1, Razdel2, Etc, SearchResultView, SignUpView
from .views import SignInView, UserProfileView, logout_view


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
    path('pozn/', Razdel1.as_view(), name='pozn'),
    path('len/', Razdel2.as_view(), name='len'),
    path('etc/', Etc.as_view(), name='etc'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('user_profile/<int:user_id>/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', logout_view, name='logout')
]
