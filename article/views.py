from django.shortcuts import render
from rest_framework.views import APIView


class ArticleDetail(APIView):
    def get(self, request, pk):
        pass