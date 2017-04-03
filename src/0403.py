import urllib2
import requests
urlp = 'http://www.kbreport.com/player/list?key=송광민'
urlb = "http://www.kbreport.com/leader/main?"
url1 = "rows=20&order=oWAR&orderType=DESC&"
url2 = "teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0"

urlbaseball = urlb + url1 + url2
print urlbaseball

data = requests.get(urlbaseball).text
print data[5000:6500]

print data.find('top-score-top')
print data.find('top-score end')

mydata = data[6803:8816 + len('top-score end')]

import re
p = re.compile(u'.승.+')
found = p.findall(mydata)
print found

for item in found:
    print item
    
import requests
urlkorea = 'http://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
data=requests.get(urlkorea).text
#print data

kosis = 'http://kosis.kr/statisticsList/statisticsList_01List.jsp?vwcd=MT_ZTITLE&parentId=A#SubCont'
data = requests.get(urlkorea).text
print len(data)