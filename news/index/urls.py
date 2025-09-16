from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('news/<int:pk>', views.news_page),
    path('category/<int:pk>/', views.category_page),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('add-to-favourite/<int:pk>', views.add_to_favourite, name='add_to_favourite'),
    path('del-from-favourite/<int:pk>', views.del_from_favourite),
    path('favourite', views.favourite_page)
]