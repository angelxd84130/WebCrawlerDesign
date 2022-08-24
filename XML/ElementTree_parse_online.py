import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1532360.xml'

hold = urllib.request.urlopen(url, context=ctx)
data = hold.read()
tree = ET.fromstring(data)
#items = tree.findall('.//comment')
items = tree.findall('.//count')
count = 0
for item in items:
    #print('Name', item.find('name').text)
    #print('Count', item.find('count').text)
    #count += int(item.find('count').text)
    print('Count', item.text)
    count += int(item.text)

print(count)
