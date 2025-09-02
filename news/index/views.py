from django.shortcuts import render
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