from rest_framework.routers import DefaultRouter
from techshamanapi import views


router = DefaultRouter()

router.register('article', views.ArticleModelViewSet, basename='article')


urlpatterns = []

urlpatterns += router.urls
