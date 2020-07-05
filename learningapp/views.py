from django.shortcuts import render
from django.http import HttpResponse
def sayhello(request):
    return HttpResponse("歡迎")
def index(request):
    return render(request,"index.html")
def coursehtml(request):
    return render(request,"coursehtml.html")
def coursecss(request):
    return render(request,"coursecss.html")
def coursejs(request):
    return render(request,"coursejs.html")
def coursejquery(request):
    return render(request,"coursejquery.html")






# Create your views here.
