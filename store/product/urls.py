from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

product_urls = router.urls