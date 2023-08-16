from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="categories")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.title
