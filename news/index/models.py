from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категория новостей'

class News(models.Model):
    news_header = models.CharField(max_length=128)
    news_text = models.TextField()
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_header

    class Meta:
        verbose_name_plural = 'Новость'