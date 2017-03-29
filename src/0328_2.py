import lxml.html
from lxml.cssselect import CSSSelector
import requests
a = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')

h = lxml.html.fromstring(a.text)

print lxml.html.tostring(h)[:1000]

s = CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
nodes = s(h)
print "node: ",len(nodes)

for node in nodes:
    print node.text
    print "------------"