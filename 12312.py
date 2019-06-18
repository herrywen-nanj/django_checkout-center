import urllib.request
import re
a = []
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
            content_first.append({'url': content_content_1['url'], 'service_name': content_content_1['server_name'],'version': content_content_1['version']})
        else:
            html = page.read().decode('utf-8')
            title = re.findall('<title>欢迎使用云平台(.+)服务</title>', html)
            if title == None:
                print("title没找到")
            else:
                service_name_version = " ".join(title)
                a.append(service_name_version.split(' ')[0])
                a.append(service_name_version.split(' ')[1])
                content_content['url'] = url
                content_content['service_name'] = a[0]
                content_content['version'] = a[1]
                content_last.append({'url': content_content['url'], 'service_name': content_content['service_name'],'version': content_content['version']})
    content_last = content_last + content_first
    print(content_last)

lines = [ 'http://10.25.1.1:80', 'http://10.25.1.1:81', 'http://10.25.1.1:82','http://10.25.1.1:83', 'http://10.25.1.2:80', 'http://10.25.1.3:80']
temp_function(lines)