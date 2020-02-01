from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Article, Category, Series, Comment
from techshamanapi.serializers import ArticleModelSerializer, SeriesModelSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class ArticleModelViewSet(ModelViewSet):
    serializer_class = ArticleModelSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete', 'patch']
    queryset = Article.objects.filter(is_published=True)
    permission_classes = [AllowAny, ]


class SeriesModelViewSet(ModelViewSet):
    serializer_class = SeriesModelSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete', 'patch']
    queryset = Series.objects.all()
    permission_classes = [AllowAny, ]
