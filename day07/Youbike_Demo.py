import json
import day07.UTI as u
file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
data = file.read()
youbike = json.loads(data)
#print(youbike)
print(youbike['retVal']['2001'])
print(youbike['retVal']['2001']['sna'])
print(youbike['retVal']['2001']['tot'])
print(youbike['retVal']['2001']['sbi'])
print(youbike['retVal']['2001']['bemp'])
print(youbike['retVal']['2001']['lat'])
print(youbike['retVal']['2001']['lng'])
# 我所在的經緯度  24.992813597959195, 121.29529097506138 桃園市桃園區法治路20號
print(u.distance(24.992813597959195, 121.29529097506138, 24.968128, 121.194666))