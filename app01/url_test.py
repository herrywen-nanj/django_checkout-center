import urllib.request
import re

def temp_function(lines):
    content_content = {}
    content_last = []
    num = 0
    #lines = [ 'http://192.168.5.148:60002','http://192.168.5.148:60002']
    for url in lines:
        try:
            page = urllib.request.urlopen(url)
        except urllib.error.URLError:
            pass
        else:
            html = page.read().decode('utf-8')
            title = re.findall('<title>欢迎使用云平台(.+)服务</title>', html)
            if title == None:
                print("title  没有找到")
            else:
                service_name_version = " ".join(title)
                a = service_name_version.split(' ')
                content_content['url'] = url
                content_content['service_name'] = a[0]
                content_content['version'] = a[1]
                content_last.append({'url': content_content['url'], 'service_name': content_content['service_name'],'version': content_content['version']})
    print(content_last)
lines = [ 'http://192.168.5.168:60032','http://192.168.5.168:60001','http://192.168.5.168:60002']
temp_function(lines)