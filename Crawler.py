import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.ptt.cc/bbs/python/index.html", verify=False)
soup = BeautifulSoup(res.text)

for detail in soup.select('.r-ent'):
    #print "日期: ", (detail.select('.date')[0].text).replace(" ", "")
    #print "作者: ", (detail.select('.author')[0].text).replace(" ", "")
    #print "標題: ", (detail.select('.title')[0].text).replace(" ", "")
    
    for a in detail.select('.title')[0].find_all('a'):
        url = "https://www.ptt.cc" + a.get('href')
        resContent = requests.get(url, verify=False)
        soupContent = BeautifulSoup(resContent.text)
        
        for content in soupContent.select('#main-content'):
            output = content.text[:content.text.index('--')]
            print "## ", output
            
        #for tag in soupContent.select('.article-metaline-right'):
        #    print "看板名稱: ", (tag.select('.article-meta-value')[0].text).replace(" ", "")

