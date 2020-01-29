from rest_framework.serializers import ModelSerializer
from blog.models import Article, Category, Series


class ArticleModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'meta', 'author', 'date_created', 'updated',
                    'body', 'is_published', 'categories', 'series', 'views']
        depth = 2
