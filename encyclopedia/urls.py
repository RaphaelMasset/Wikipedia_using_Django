from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CPP", views.CPP, name="CPP"), 
    path("CSS", views.CSS, name="CSS"),
    path("Django", views.Django, name="Django"),
    path("HTML", views.HTML, name="HTML"),
    path("Python", views.Python, name="Python"),
    path("Git", views.Git, name="Git"),
    
    path("<str:searchQuery>", views.search, name="search")
     
]


