from django.shortcuts import render, redirect
from .models import Category, News, Favourite
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


def add_to_favourite(request, pk):
    if request.method == 'POST':
        favourite_news = News.objects.get(id=pk)
        user_have = int(request.POST.get('true_or_false'))
        if user_have == 0:
            Favourite.objects.create(user_id=request.user.id,
                                     favourite_news=favourite_news,
                                     have_favourite=True).save()
            return redirect('/')
        if user_have == 1:
            Favourite.objects.create(user_id=request.user.id,
                                     favourite_news=favourite_news,
                                     have_favourite=False).save()
            return redirect('/')
        return redirect(f'/news_page/{pk}')

def favourite_page(request):
    favourite_news = Favourite.objects.filter(user_id=request.user.id,
                                              have_favourite=True)
    categories = Category.objects.all()
    context = {
        'favourite_news': favourite_news,
        'categories': categories,
    }

    return render(request, 'favourite_page.html', context)