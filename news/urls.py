from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, NewsViewSet

router = SimpleRouter()
router.register(r"news", NewsViewSet, basename="news")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = router.urls

app_name = "news"
