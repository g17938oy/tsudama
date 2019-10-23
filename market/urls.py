from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('talk/', views.talk, name='talk'),
]
