from django.shortcuts import render
from unicodedata import category

from .models import Category, News


# Create your views here.

def home_page (request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'home.html', context)

def news_page (request, pk):
    news = News.objects.get(id=pk)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'news_page.html', context)

def category_page (request, pk):
    categories = Category.objects.get(id=pk)
    news = News.objects.filter(news_category=categories)
    all_categories = Category.objects.all()
    context = {
        'categories': categories,
        'news': news,
        'all_categories': all_categories
    }
    return render(request, 'news_on_category.html', context)