from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.


def index(request):
    s = get_template('testApp/index2.html')
    html = s.render()

    return HttpResponse(html)

def index2(request):
    s = get_template('testApp/index2.html')
    html = s.render()

    return HttpResponse(html)


def xueyuan(request):
    s = get_template('testApp/xueyuan.html')
    html = s.render()

    return HttpResponse(html)

def zhuanye(request):
    s = get_template('testApp/zhuanye.html')
    html = s.render()

    return HttpResponse(html)

def hangye(request):
    s = get_template('testApp/hangye.html')
    html = s.render()

    return HttpResponse(html)

def yuce(request):
    s = get_template('testApp/yuce.html')
    html = s.render()

    return HttpResponse(html)