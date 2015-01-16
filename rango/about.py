from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>This tutorial has been put together by Terence Aqachmar 2087939a</strong><br/>"
                        + "Rango says here is the about page! <br/> "
                        + "<a href='/rango/'>Index</a>")
