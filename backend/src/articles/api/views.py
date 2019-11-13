from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Article
from .serializers import ArticleSerializer


class ListArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ListDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
