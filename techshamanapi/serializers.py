from rest_framework.serializers import ModelSerializer
from blog.models import Article, Category, Series


class ArticleModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 2


class SeriesModelSerializer(ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
