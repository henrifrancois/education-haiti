from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

# Create your views here.

def programs(request):
    "Renders the programs page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'programs.html',
        context_instance=RequestContext(request,
        {
            'title': 'Home',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )

def about(request):
    "Renders the programs page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        context_instance=RequestContext(request,
        {
            'title': 'Home',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )