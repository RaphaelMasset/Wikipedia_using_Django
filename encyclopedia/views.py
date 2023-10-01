from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from markdown2 import Markdown

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
                "HTML_code":  "<h2> entry not found </h2>"
            })


def search(request):
    markdowner = Markdown()
    superstring_list = []
    nbResult = 0

    if request.method == "POST":
        search_request = request.POST['q']

        if search_request in util.list_entries():
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

