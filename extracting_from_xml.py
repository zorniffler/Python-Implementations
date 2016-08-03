import urllib
from BeautifulSoup import *
import xml.etree.ElementTree as ET

url='http://python-data.dr-chuck.net/comments_294914.xml'
xml=urllib.urlopen(url).read()
datos= ET.fromstring(xml)
lst= datos.findall('comments/comment')

sum=0
for elem in lst:
	sum=sum+int(elem.find('count').text)
print sum