from django.urls import path
from .views import TagListCreateView, CategoryListCreateView, ArticleListCreateView, ArticleDetailView, TagDetailView, CategoryDetailView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('articles/tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('articles/categorys/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('articles/categorys/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]