import json
import day07.UTI as u
file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
data = file.read()
youbike = json.loads(data)
#print(youbike)
no = 3003
sno = str(no)
try:
    print(youbike['retVal'][sno])
    print(youbike['retVal'][sno]['sno'])
    print(youbike['retVal'][sno]['sna'])
    print(youbike['retVal'][sno]['tot'])
    print(youbike['retVal'][sno]['sbi'])
    print(youbike['retVal'][sno]['bemp'])
    print(youbike['retVal'][sno]['lat'])
    print(youbike['retVal'][sno]['lng'])
except:
    print('無此站台: %s' % sno)
# 我所在的經緯度  24.992813597959195, 121.29529097506138 桃園市桃園區法治路20號
print(u.distance(24.992813597959195, 121.29529097506138, 24.968128, 121.194666))