from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title