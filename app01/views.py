from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from app01 import temp_function
import urllib.request
import re

# Create your views here.
def test_138(request):
    lines = ['http://192.168.5.138:60001', 'http://192.168.5.138:60002', 'http://192.168.5.138:60003',
             'http://192.168.5.138:60004', 'http://192.168.5.138:60005', 'http://192.168.5.138:60006',
             'http://192.168.5.138:60008', 'http://192.168.5.138:60011', 'http://192.168.5.138:60014',
             'http://192.168.5.138:60016', 'http://192.168.5.138:60019', 'http://192.168.5.138:60021',
             'http://192.168.5.138:60023', 'http://192.168.5.138:60025', 'http://192.168.5.138:60026',
             'http://192.168.5.138:60032']
    content_last = temp_function.temp_function(lines)
    return render(request, "test.html", {"list": content_last})


def test_148(request):
    lines = ['http://192.168.5.148:60001', 'http://192.168.5.148:60002', 'http://192.168.5.148:60003','http://192.168.5.148:60004', 'http://192.168.5.148:60005', 'http://192.168.5.148:60006','http://192.168.5.148:60008', 'http://192.168.5.148:60011', 'http://192.168.5.148:60014','http://192.168.5.148:60016', 'http://192.168.5.148:60019', 'http://192.168.5.148:60021','http://192.168.5.148:60023', 'http://192.168.5.148:60025', 'http://192.168.5.148:60026','http://192.168.5.148:60032']
    content_last = temp_function.temp_function(lines)
    return render(request, "test.html", {"list": content_last})

def test_158(request):
    lines = ['http://192.168.5.158:60001', 'http://192.168.5.158:60002', 'http://192.168.5.158:60003',
             'http://192.168.5.158:60004', 'http://192.168.5.158:60005', 'http://192.168.5.158:60006',
             'http://192.168.5.158:60008', 'http://192.168.5.158:60011', 'http://192.168.5.158:60014',
             'http://192.168.5.158:60016', 'http://192.168.5.158:60019', 'http://192.168.5.158:60021',
             'http://192.168.5.158:60023', 'http://192.168.5.158:60025', 'http://192.168.5.158:60026',
             'http://192.168.5.158:60032']
    content_last = temp_function.temp_function(lines)
    return render(request, "test.html", {"list": content_last})

def test_168(request):
    lines = ['http://192.168.5.168:60001', 'http://192.168.5.168:60002', 'http://192.168.5.168:60003',
             'http://192.168.5.168:60004', 'http://192.168.5.168:60005', 'http://192.168.5.168:60006',
             'http://192.168.5.168:60008', 'http://192.168.5.168:60011', 'http://192.168.5.168:60014',
             'http://192.168.5.168:60016', 'http://192.168.5.168:60019', 'http://192.168.5.168:60021',
             'http://192.168.5.168:60023', 'http://192.168.5.168:60025', 'http://192.168.5.168:60032']
    content_last = temp_function.temp_function(lines)
    return render(request, "test.html", {"list": content_last})

def test__148(request):
    lines = ['http://192.168.1.148:60001','http://192.168.1.148:60002','http://192.168.1.148:60003','http://192.168.1.148:60004','http://192.168.1.148:60005','http://192.168.1.148:60006','http://192.168.1.148:60008','http://192.168.1.148:60011','http://192.168.1.148:60014','http://192.168.1.148:60016','http://192.168.1.148:60019','http://192.168.1.148:60021','http://192.168.1.148:60023','http://192.168.1.148:60025','http://192.168.1.148:60026']
    content_last = temp_function.temp_function(lines)
    return render(request,"test.html",{"list":content_last})

def test__158(request):
    lines = ['http://192.168.1.158:60001','http://192.168.1.158:60002','http://192.168.1.158:60003','http://192.168.1.158:60004','http://192.168.1.158:60005','http://192.168.1.158:60006','http://192.168.1.158:60008','http://192.168.1.158:60011','http://192.168.1.158:60014','http://192.168.1.158:60016','http://192.168.1.158:60019','http://192.168.1.158:60021','http://192.168.1.158:60023','http://192.168.1.158:60025','http://192.168.1.158:60026']
    content_last = temp_function.temp_function(lines)
    return render(request,"test.html",{"list":content_last})

def test__168(request):
    lines = ['http://192.168.1.168:60001','http://192.168.1.168:60002','http://192.168.1.168:60003','http://192.168.1.168:60004','http://192.168.1.168:60005','http://192.168.1.168:60006','http://192.168.1.168:60008','http://192.168.1.168:60011','http://192.168.1.168:60014','http://192.168.1.168:60016','http://192.168.1.168:60019','http://192.168.1.168:60021','http://192.168.1.168:60023','http://192.168.1.168:60025','http://192.168.1.168:60026']
    content_last = temp_function.temp_function(lines)
    return render(request,"test.html",{"list":content_last})



#汇总函数
def sumer(request):
    return render(request,"base.html")