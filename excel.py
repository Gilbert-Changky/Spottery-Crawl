# import xlwt
# f = open('Data.txt','r')
# text = f.read()
# f.close()

import xlwt
text = []
f = open('Data.txt','r')
all = []
for line in f:
    line.replace(' ','')
    i = line.split(' [')[1]
    print (i)
    theList = i.strip(',').split(',')
    # print(theList)

    a1 = theList[0]
    a2 = theList[1][2:4]
    a3 = theList[2][2:4]
    a4 = theList[3][1]
    a5 = theList[4][1]
    a6 = theList[5].split(']')[0].replace(' ','')
    single = []
    single.append(a1)
    single.append(a2)
    single.append(a3)
    single.append(a4)
    single.append(a5)
    single.append(a6)
    all.append(single)

f.close()
print (all)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('test', cell_overwrite_ok=True)
counting = 0
for i in all:
    counting += 1
    for j in range(0,len(i)):
        sheet.write(counting, j, i[j])
        j += 1
book.save('data.xls')

# image_list = image.strip(',').split(',')