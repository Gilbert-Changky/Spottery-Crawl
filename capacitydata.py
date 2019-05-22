import re

def capacitydata():
    f = open('capacitySource.txt','r')
    html = f.read()
    f.close

    Namelist = []
    dict = {}
    dict0 = {}
    dict1 = {}
    chineseName = ['巴塞罗那', '皇家马德里', '巴伦西亚', '塞维利亚', '赫塔费', '比利亚雷亚尔', '毕尔巴鄂竞技', '马德里竞技', '拉科鲁尼亚', '西班牙人', '马拉加',
                       '皇家社会', '皇家贝蒂斯', '莱万特', '塞尔塔', '莱加内斯', '拉斯帕尔马斯', '阿拉维斯', '赫罗纳', '埃瓦尔'
                       ]
    engName = ['FC Barcelona', 'Real Madrid', 'Valencia CF', 'Sevilla FC', 'Getafe CF', 'Villarreal CF',
                   'Athletic Bilbao', 'Atlético Madrid', 'RC Deportivo', 'RCD Espanyol', 'Málaga CF', 'Real Sociedad',
                   'Real Betis', 'Levante UD', 'Celta Vigo', 'CD Leganés', 'UD Las Palmas', 'Deport. Alavés',
                   'Girona CF', 'SD Eibar'
                   ]

    capacityData = re.findall('<td data-title="OVR"><span class="label rating r\d">(.*?)</span>',html,re.S)
    capacityName0 = re.findall('<td data-title="Name">(.*?)</a></td>',html,re.S)
    for i in capacityName0:
        capacityName = re.findall('>(.*)',i,re.S)
        Namelist.append(capacityName[0])

    for i in range(0,len(Namelist)):
        dict0[Namelist[i]] = capacityData[i]

    for i in range(0,len(Namelist)):
        dict1[chineseName[i]] = engName[i]

    for i in range(0,len(Namelist)):
        dict[chineseName[i]] = dict0[dict1[chineseName[i]]]

    return dict
