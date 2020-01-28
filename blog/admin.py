from django.contrib import admin
from blog.models import Article, Category, Series


class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'categories', 'series']
    fields = ['title', 'slug', 'meta', 'author', 'date_created', 'updated',
             'body', 'is_published', 'categories', 'series', 'views']
    readonly_fields = ['date_created', 'updated']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']


class SeriesAdmin(admin.ModelAdmin):
    fields = ['series']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Series,SeriesAdmin)
admin.site.register(Category, CategoryAdmin)
