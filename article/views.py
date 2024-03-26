from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from article.models import Article
from rest_framework.response import Response
from rest_framework import status
from rest_framework import pagination


class ArticleDetailView(APIView):
    def get(self, request, pk):
        articles = get_list_or_404(Article, id=pk)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ArticleCreateView(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ArticleUpdateView(APIView):
    def put(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ArticleDeleteView(APIView):
    def delete(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticlePagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class ArticleListView(APIView):
    pagination_class = ArticlePagination
    
    def get(self, request):
        articles = Article.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(articles, request)
        serializer = ArticleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)