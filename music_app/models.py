
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.SlugField(primary_key=True)
    def __str__(self):
        return self.title


class Music(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'),
        ('KZ', 'Казахстан')
    )
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=50)
    descrption = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')
    duration = models.IntegerField()
    country = models.CharField(max_length=30, choices=COUNTRY)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.category}'
