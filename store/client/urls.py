from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')

client_urls = router.urls