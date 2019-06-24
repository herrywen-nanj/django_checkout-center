import urllib.request
import re


def temp_function():
    content_content_1 = {}
    content_content = {}
    content_last = []
    content_first = []
    lines = ['http://192.168.1.1:80', 'http://192.168.1.1:81', 'http://192.168.1.1:82',
             'http://192.168.1.2:80', 'http://192.168.1.2:81', 'http://192.168.1.2:82',
             'http://192.168.1.2:83', 'http://192.168.1.3:80', 'http://192.168.1.3:81',
             'http://192.168.1.3:82', 'http://192.168.1.3:84', 'http://192.168.1.3:60009',
             'http://192.168.1.4:80', 'http://192.168.1.4:81', 'http://192.168.1.4:82',
             'http://192.168.1.5:80', 'http://192.168.1.5:81', 'http://192.168.1.5:82',
             'http://192.168.1.5:83', 'http://192.168.1.5:88', 'http://192.168.2.1:80',
             'http://192.168.2.1:81', 'http://192.168.2.1:82', 'http://192.168.2.2:80',
             'http://192.168.2.2:81', 'http://192.168.2.2:82', 'http://192.168.2.2:83',
             'http://192.168.2.3:80', 'http://192.168.2.3:81', 'http://192.168.2.3:82',
             'http://192.168.2.3:84', 'http://192.168.2.3:60009', 'http://192.168.2.4:80',
             'http://192.168.2.4:81', 'http://192.168.2.4:82', 'http://192.168.2.5:80',
             'http://192.168.2.5:81', 'http://192.168.2.5:82', 'http://192.168.2.5:83',
             'http://192.168.2.5:88', 'http://192.168.2.10:80', 'http://192.168.2.11:80']
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
    print(content_last)

temp_function()