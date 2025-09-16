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

class Favourite(models.Model):
    user_id = models.IntegerField()
    favourite_news = models.ForeignKey(News, on_delete=models.CASCADE)
    have_favourite = models.BooleanField(default=False)


    def __str__(self):
        return str(self.favourite_news)

    class Meta:
        verbose_name_plural = 'Избранное'