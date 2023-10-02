from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from markdown2 import Markdown
import random

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    markdowner = Markdown()

    if title in util.list_entries():
        return render(request, f"encyclopedia/entry.html", {
            "title": title,
            "HTML_code":  markdowner.convert(util.get_entry(title))
        })

    else:
        return render(request, f"encyclopedia/entry.html", {
                "title": "error",
                "HTML_code":  "<h2>error: entry not found </h2>"
            })

def newPage(request):
    markdowner = Markdown()
    if request.method == "POST":
        titleInput = request.POST['titleInput']
        textInput = request.POST['textInput']
        if util.get_entry(titleInput) != None:
            return render(request, f"encyclopedia/entry.html", {
                "title": "error",
                "HTML_code":  "<h2>error: this title already exist </h2>"
            })
        else:
            util.save_entry(titleInput, textInput)
            return render(request, f"encyclopedia/entry.html", {
                "title": titleInput,
                "HTML_code": markdowner.convert(textInput)
            })
    else:
        return render(request, "encyclopedia/newPage.html", {
            })
    



def search(request):  
    markdowner = Markdown()
    superstring_list = []
    nbResult = 0

    #tp make the search case insensitiv
    entry_upper = [x.upper() for x in util.list_entries()] 

    if request.method == "POST":
        search_request = request.POST['q'].upper()

        if search_request in entry_upper:
            return render(request, "encyclopedia/entry.html", {
                "title": search_request,
                "HTML_code":  markdowner.convert(util.get_entry(search_request))
            })
        
        else:
            for entry in util.list_entries():
                if search_request in entry:
                    superstring_list.append(entry)
                    nbResult +=1

            return render(request, "encyclopedia/searchResult.html", {
                "entries": superstring_list,
                "nbResult": nbResult
            })

def randm(request): 
    markdowner = Markdown()
    title = random.choice(util.list_entries())
    return render(request, f"encyclopedia/randm.html", {
        "title": title,
        "HTML_code":  markdowner.convert(util.get_entry(title))
    })