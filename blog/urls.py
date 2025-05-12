from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('category/<slug:slug>/', views.CategoryPostsView.as_view(), name='category_posts'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
