import capacitydata
import re
import requests

def searchMatch():
    list = []
    for page in range(1,13):
        dict = capacitydata.capacitydata()
        dict['维戈塞尔塔'] = '80'
        url = 'http://info.sporttery.cn/football/match_result.php'
        data = {
            'start_date': '2017-07-01',
            'end_date': '2018-07-19',
            'search_league': '62',
            'page':page
        }

        # get the source of page
        html = requests.post(url, data = data)
        html.encoding = 'GBK'
        html = html.text

        # find the result of single match.
        matchResult = re.findall('style="font-weight:bold; font-size:13px;">(.*?)</span></td>',html,re.S)
        GD = []
        # GD is list of game difference.
        for i in range(0,len(matchResult)):
            item = matchResult[i]
            result = int(item[0]) - int(item[2])
            GD.append(result)

        # Get the link of the
        link = []
        linkRange = re.findall('<td width="300"(.*?)</td>',html,re.S)
        for i in range(0,len(linkRange)):
            link.append(re.findall('<a href="(.*?)" target="_blank"',linkRange[i],re.S))

        house = re.findall('<span class="zhu" style="width:128px" title="(.*?)">',html,re.S)

        away = re.findall('<span style="width:128px" class="ke" title="(.*?)">',html,re.S)


        matchData = []


        for i in range(len(house)):
            singleData = []
            houseCapacity = dict[str(house[i])]
            awayCapacity = dict[away[i]]
            singleData.append(house[i])
            singleData.append(houseCapacity)
            singleData.append(away[i])
            singleData.append(awayCapacity)
            singleData.append(GD[i])
            singleData.append(link[i])
            matchData.append(singleData)

        for k in matchData:
            list.append(k)

    matchData = list

    return  matchData

# f = open('searchMatch.txt','w')
# for i in searchMatch():
#     f.write(str(i))
# f.close()

# print(searchMatch())
# data1 = searchMatch()[1:5]
# print(data1)
