from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("newPage", views.newPage, name="newPage"),
    path("search", views.search, name="search"),
    path("randm", views.randm, name="randm"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("save", views.save, name="save"),
    
    path("<str:title>", views.entry, name="entry")


    
]


    