from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from news.models import News, Category
from news.serializers import NewsSerializer

NEWS_URL = reverse("news:news-list")


def detail_url(news_id: int):
    return reverse("news:news-detail", args=[news_id])


class UnauthenticatedMovieApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(NEWS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


def sample_category(**params):
    defaults = {
        "name": "Test Category",
    }
    defaults.update(params)
    return Category.objects.create(**defaults)


def sample_news(**params):
    defaults = {
        "title": "Test News",
        "content": "Test content",
        "image": None,
        "created_at": "2023-08-17T08:08:01.114961Z",
        "updated_at": "2023-08-17T08:08:01.114961Z",
        "category": params,
        "author": params,
    }
    defaults.update(params)
    return News.objects.create(**defaults)


class AuthenticatedNewsApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test2@test.com",
            "testuser",
        )
        self.client.force_authenticate(self.user)

    def test_list_news(self):
        sample_news(author=self.user, category=sample_category())

        res = self.client.get(NEWS_URL)

        news_instance = News.objects.get(pk=1)
        serializer = NewsSerializer(news_instance)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(res.data["results"][0]), serializer.data)

    def test_filter_news_by_category(self):
        hot_category = sample_category(name="Hot")
        sport_category = sample_category(name="Sport")

        news1 = sample_news(author=self.user, category=hot_category)
        news2 = sample_news(author=self.user, category=sport_category)

        res = self.client.get(NEWS_URL, {"category": hot_category.id})

        serializer1 = NewsSerializer(news1)
        serializer2 = NewsSerializer(news2)

        hot_category_news = [serializer1.data] if hot_category.name == "Hot" else []
        sport_category_news = (
            [serializer2.data] if sport_category.name == "Sport" else []
        )

        expected_data = hot_category_news + sport_category_news

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(res.data["results"][0]), expected_data[0])
