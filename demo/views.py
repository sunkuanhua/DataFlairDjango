from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
   return HttpResponse("DataFlair Django kuan hua Tutorial<html><body><h1> Hello World DataFlair Dango skh tutorials</body></html>")

def data_flair(request):
    return redirect('/dataflair')

def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django cookie enabled Tutorial</h1>")
    html.set_cookie('demo', 'Hello this is your Cookies', max_age = None)
    return html

def showcookie(request):
    show = request.COOKIES['demo']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)