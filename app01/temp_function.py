from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
import urllib.request
import re

def temp_function(lines):
    content_content_1 = {}
    content_content = {}
    content_last = []
    content_first = []
    for url in lines:
        try:
            page = urllib.request.urlopen(url)
        except urllib.error.URLError:
            content_content_1['url'] = url
            content_content_1['server_name'] = ''
            content_content_1['version'] = ''
            content_first.append({'url': content_content_1['url'], 'service_name': content_content_1['server_name'],
                                  'version': content_content_1['version']})
        else:
            html = page.read().decode('utf-8')
            title = re.findall('<title>欢迎使用云平台(.+)服务</title>', html)
            if title:
                service_name_version = " ".join(title)
                content_content['url'] = url
                content_content['service_name'] = service_name_version.split(' ')[0]
                content_content['version'] = service_name_version.split(' ')[1]
                content_last.append({'url': content_content['url'], 'service_name': content_content['service_name'],'version': content_content['version']})
    content_last = content_last + content_first
    return content_last