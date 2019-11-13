from django.urls import path
from .views import ListArticleView, ListDetailView

urlpatterns = [
    path('', ListArticleView.as_view()),
    path('<pk>', ListDetailView.as_view()),
]
