import urllib
keyword = '비오는'
f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
mydata = f.read();

import lxml.html
from lxml.cssselect import CSSSelector

html = lxml.html.fromstring(mydata)
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')
nodes = sel(html)
for node in nodes:
    print node.text_content()