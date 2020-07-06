from django.conf import settings
from django.db import models
from product.models import Product

class Order(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    items = models.ManyToManyField(Product)