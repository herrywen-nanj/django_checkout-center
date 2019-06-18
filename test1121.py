# a = [1,2,3,4,5,6]
# b = [ 'a','d','s', 'a', 'd','a' ,'s', 'd' ,'a','s']
# print(a+b)
import urllib.request
import re

def temp_function():
    content_content = {}
    content_content_1 = {}
    content_last = []
    content_first = []
    lines = ['http://192.168.5.138:60001', 'http://192.168.5.138:60002', 'http://192.168.5.138:50026', 'http://192.168.5.138:60003','http://192.168.5.138:60004', 'http://192.168.5.138:60005', 'http://192.168.5.138:60006','http://192.168.5.138:60008', 'http://192.168.5.138:60011', 'http://192.168.5.138:60014','http://192.168.5.138:60016', 'http://192.168.5.138:60019', 'http://192.168.5.138:60021','http://192.168.5.138:60023', 'http://192.168.5.138:60025', 'http://192.168.5.138:60026','http://192.168.5.138:60032', 'http://192.168.5.138:60033']
    for url in lines:
        try:
            page = urllib.request.urlopen(url)
        except urllib.error.URLError:
            print("url链接是{}".format(url))
            content_content_1['url'] = url
            content_content_1['server_name'] = ''
            content_content_1['version'] = ''
            content_first.append({'url': content_content_1['url'], 'service_name': content_content_1['server_name'], 'version': content_content_1['version']})
        else:
            html = page.read().decode('utf-8')
            title = re.findall('<title>欢迎使用云平台(.+)服务</title>', html)
            if title == None:
                print("title没找到")
            else:
                service_name_version = " ".join(title)
                a = service_name_version.split(' ')
                content_content['url'] = url
                content_content['service_name'] = a[0]
                content_content['version'] = a[1]
                content_last.append({'url': content_content['url'], 'service_name': content_content['service_name'],'version': content_content['version']})
    content_last = content_last + content_first
    print(content_last)


temp_function()