
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("book/",views.book_table,name="book"),
    path("menu/",views.menu,name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
    path('success/', views.success, name='success'),
]