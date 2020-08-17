from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template.loader import get_template
# Create your views here.

def index2(request):
    s = get_template('testApp/index2.html')
    html = s.render()

    return HttpResponse(html)