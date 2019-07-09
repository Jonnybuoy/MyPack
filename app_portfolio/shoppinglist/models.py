from __future__ import unicode_literals
from django.db import models
# from datetime import datetime
from django.utils import timezone


class Shoppinglist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
