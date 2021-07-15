name = "height"
value = 170
print(name, value) # 中間預設使用空白隔開
print(name, value, sep="=") # 中間使用 = 隔開

height = "身高"
h = 170
weight = "體重"
w = 60
print(height, h, sep="=", end="&") #使用& 符號解委
print(weight, w, sep="=") #使用預設換行符號結尾

print("--------------------")
# 匯率列表
symbol1 = "2330.TW"
price1 = 650
amount1 = 4500
total1 = price1 * amount1

symbol2 = "1101.TW"
price2 = 53
amount2 = 1200
total2 = price2 * amount2
# 資料對齊
print("--------------------")
print(symbol1, price1, amount1, total1)
print(symbol2, price2, amount2, total2)
print("--------------------")
print("%4d" % 7)
print("%4d" % 77)
print("%4d" % 777)
print("%4d" % 7777)
print("%-4d" % 7)
print("%-4d" % 77)
print("%-4d" % 777)
print("%-4d" % 7777)


