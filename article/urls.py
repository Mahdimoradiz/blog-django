from django.urls import path
from . import views


urlpatterns = [
    path('article/<int:pk>', views.ArticleDetail.as_view(), name="article_detail"),
]
