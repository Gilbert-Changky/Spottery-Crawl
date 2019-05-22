from selenium import webdriver
import re

url = 'http://info.sporttery.cn/football/info/fb_match_info.php?m=108193'
def getHtml(url):
    driver = webdriver.PhantomJS(executable_path='/Users/Noble.Zhang/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.get(url)
    html = driver.page_source
    return html

def total(url):
    getHtml(url)
    html = getHtml(url)
    usefulHtmlHome = re.findall('<tbody id="homeInfos">(.*?)</tbody>', html, re.S)
    usefulHtmlAway = re.findall('<tbody id="awayInfos">(.*?)</tbody>', html, re.S)
    usefulHtmlHistory = re.findall('<tbody id="HistoryInfos">(.*?)</tbody>', html, re.S)

    HomeData = searchPastMatch(findSource(usefulHtmlHome)[0], findSource(usefulHtmlHome)[1])
    AwayData = searchPastMatch(findSource(usefulHtmlAway)[0], findSource(usefulHtmlAway)[1])
    HistoryData = searchPastMatch(findSource(usefulHtmlHistory)[0], findSource(usefulHtmlHistory)[1])

    return HomeData,AwayData,HistoryData

def findSource(usefulHtml):
    homeName = []
    matchResult = []

    homeDataSource = re.findall('<td><a title="(.*?)" class="',usefulHtml[0],re.S)
    i = 0
    while i <= (len(homeDataSource)-2):
        homeName.append(homeDataSource[i])
        i += 2
    matchResult = re.findall('" target="_blank">(.*?)</a></td>',usefulHtml[0],re.S)
    return matchResult,homeName

def searchPastMatch(matchResult,homeName):
    count = []
    n = 0
    for i in matchResult:
        n += 1
        if '20' in i:
            count.append(n)

    s1 = 0
    s2 = 1
    matchData = []

    while s2 < len(count):
        singleData = []
        t1 = count[s1]-1
        t2 = count[s2]-1
        while t1 < t2:
            singleData.append(matchResult[t1])
            t1 += 1
        matchData.append(singleData)
        s1 += 1
        s2 += 1

    r1 = 0
    while r1 < len(matchData):
        matchData[r1].pop(1)
        matchData[r1].insert(1,homeName[r1])
        r1 += 1

    for i in matchData:
        if ':' not in i[2]:
            matchData.remove(i)

    for i in matchData:
        i.pop(3)
        i.pop(0)

    return matchData

# print(total(url))