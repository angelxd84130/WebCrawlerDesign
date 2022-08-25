import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1532361.json'

connect = urllib.request.urlopen(url, context=ctx)
data = connect.read().decode()
js = json.loads(data)
print(data)

count = 0
for item in js['comments']:
    print('Count', item['count'])
    count += int(item['count'])

print(count)
