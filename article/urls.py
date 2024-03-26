from django.urls import path
from . import views


urlpatterns = [
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name="article_detail"),
    path('article/list', views.ArticleListView.as_view(), name="article_list"),
    path('article/create', views.ArticleCreateView.as_view(), name="article_create"),
    path('article/delete/<int:pk>', views.ArticleDeleteView.as_view(), name="article_delete"),
    path('article/update/<int:pk>', views.ArticleUpdateView.as_view(), name="article_update"),
]
