from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newPage", views.newPage, name="newPage"),
    path("search", views.search, name="search"),
    
    path("<str:title>", views.entry, name="entry")


    
]


    