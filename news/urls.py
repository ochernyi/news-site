from django.urls import path
from .views import CategoryList, NewsList, NewsDetail, NewsCreate

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/create/', NewsCreate.as_view(), name='news-create'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
]

app_name = "news"
