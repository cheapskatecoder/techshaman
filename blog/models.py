from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    meta = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category')
    series = models.ManyToManyField('Series')
    views = models.IntegerField(null=True, blank=True)
    comments = models.ManyToManyField('comment', null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.views)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Category(models.Model):
    category_logo = models.FileField(upload_to='category_logo')
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Series(models.Model):
    series = models.CharField(max_length=255)

    def __str__(self):
        return self.series

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comment = RichTextField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
