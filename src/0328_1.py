import requests
response = requests.get('http://python.org/')
_html = response.text
print len(_html)