from django.contrib import admin
from blog.models import Article, Category, Series, Comment


class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'categories', 'series', 'comments']
    fields = ['title', 'slug', 'meta', 'author', 'date_created', 'updated',
             'body', 'is_published', 'categories', 'series', 'views', 'comments']
    readonly_fields = ['date_created', 'updated']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category', 'category_logo']


class SeriesAdmin(admin.ModelAdmin):
    fields = ['series']


class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'comment']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Series,SeriesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
