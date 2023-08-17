import os
import uuid

from django.db import models
from django.utils.text import slugify

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


def news_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/news/", filename)


class News(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(upload_to=news_image_file_path)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_news"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_news")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "news"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
