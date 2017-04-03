import urllib
uResponse = urllib.urlopen('http://python.org/')
_html = uResponse.read()
print len(_html)
print uResponse.info()