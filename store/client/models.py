from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name