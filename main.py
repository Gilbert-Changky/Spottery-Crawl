import re
import xlwt
import time
import requests
import searchMatch
import oneSideHistory

data = searchMatch.searchMatch()


def getgoalD(Name,dataList):

    # if Name[i]
    goalD = []
    for i in dataList:
        if i[0] == Name:
            goalD.append(int(i[1][0]) - int(i[1][2]))
        else:
            goalD.append(int(i[1][2]) - int(i[1][0]))

    GD = 0
    for i in goalD:
        GD += i

    return GD

def getWin(Name,dataList):
    countWin = 0
    for i in dataList:
        judge = int(i[1][0]) - int(i[1][2])
        if i[0] == Name:
            if judge > 0:
                countWin += 1
        else:
            if judge < 0:
                countWin += 1
    return countWin


def handleSideData(NameHome,NameAway,url):
    home = oneSideHistory.total(url)[0]
    homeGD = getWin(NameHome,home)
    # print(home)
    away = oneSideHistory.total(url)[1]
    awayGD = getWin(NameAway,away)
    # print(away)
    history = oneSideHistory.total(url)[2]
    historyGD = getgoalD(NameHome,history)

    return homeGD,awayGD,historyGD

time0 = time.localtime( time.time())
print (time0)


count = 1
allData = []

data1 = data[0:379]
for i in data1:
    singleMatch = []
    singleMatch.append(i[4])
    singleMatch.append(i[1])
    singleMatch.append(i[3])
    list = handleSideData(i[0],i[2],i[5][0])
    # print(i)
    singleMatch.append(list[0])
    singleMatch.append(list[1])
    singleMatch.append(list[2])
    count += 1
    allData.append(singleMatch)
    print (count,singleMatch)
    list = []



book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('test', cell_overwrite_ok=True)
counting = 0
for i in list:
    counting += 1
    for j in range(0,len(i)):
        sheet.write(counting, j, i[j])
        j += 1
book.save('data.xls')

time1 = time.localtime(time.time())
print(time1)
print(allData)


        #                     _ooOoo_
        #                    o8888888o
        #                    88" . "88
        #                    (| -_- |)
        #                    O\  =  /O
        #                 ____/`---'\____
        #               .'  \\|     |//  `.
        #              /  \\|||  :  |||//  \
        #             /  _||||| -:- |||||-  \
        #             |   | \\\  -  /// |   |
        #             | \_|  ''\---/''  |   |
        #             \  .-\__  `-`  ___/-. /
        #           ___`. .'  /--.--\  `. . __
        #        ."" '<  `.___\_<|>_/___.'  >'"".
        #       | | :  `- \`.;`\ _ /`;.`/ - ` : | |
        #       \  \ `-.   \_ __\ /__ _/   .-` /  /
        #  ======`-.____`-.___\_____/___.-`____.-'======
        #                     `=---='
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #               Buddha Bless, No Bug !