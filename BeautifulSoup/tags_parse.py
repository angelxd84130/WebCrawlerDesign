from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1532358.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags: 'a'/ 'span'/ 'h1'/ 'h2'...
tags = soup('span')  
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('Attrs:', tag.attrs)
    print('URL:', tag.url)
    print('Contents:', tag.contents) # list of conents
    print('Content:', tag.contents[0]) # 1st element of contents
    print('Content:', tag.content) #None
