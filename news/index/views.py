from django.shortcuts import render, redirect
from .models import Category, News
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View

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

class Register(View):
    template_file = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_file, context)

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
            return redirect('/')


# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('/')