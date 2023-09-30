from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request, searchQuery=None):
    # Check if a valid search query is provided in the URL.
    if searchQuery:
        # Define a list of valid topic names (e.g., "CPP," "CSS," "Django," etc.).
        valid_topics = util.list_entries()

        # Check if the provided searchQuery matches a valid topic name.
        if searchQuery in valid_topics:
            # If it matches, render the corresponding HTML page.
            return render(request, f"{searchQuery}.html", {
                f"{searchQuery}_text":  util.get_entry(searchQuery) 
            })

    # If no valid query or matching topic is found, raise a 404 error.
    raise Http404("Page not found")




def CPP(request):  
    return render(request, "encyclopedia/CPP.html", {
        "CPP_text":  util.get_entry("CPP") 
    })

def CSS(request):   
    return render(request, "encyclopedia/CSS.html", {
        "CSS_text":  util.get_entry("CSS") 
    })

def HTML(request):   
    return render(request, "encyclopedia/HTML.html", {
        "HTML_text":  util.get_entry("HTML") 
    })

def Python(request):   
    return render(request, "encyclopedia/Python.html", {
        "Python_text":  util.get_entry("Python") 
    })

def Django(request):   
    return render(request, "encyclopedia/Django.html", {
        "Django_text":  util.get_entry("Django") 
    })

def Git(request):   
    return render(request, "encyclopedia/Git.html", {
        "Git_text":  util.get_entry("Git") 
    })


