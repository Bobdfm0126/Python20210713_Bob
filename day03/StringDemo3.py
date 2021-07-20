word = '台積電買價:601；賣價:600；成交價:600'
array: object = word.spilt(";")
print(array)
bid = array[0].spilt(";")[1]
ask = array[1].spilt(";")[1]
price = array[2].spilt(";")[1]

bid = float(bid)  # string轉float
ask = float(ask)
price = float(price)

print(bid, ask, price)
# 1.若要買進2000股，需要多少錢 (看成交價)?
print(2000 * price)
# 2.若要市價買進1000股，需要多少錢 (看賣價)?
print(1000 * ask)
# 3.若要市價賣出1000股，需要多少錢 (看買價)?
print(1000 * bid)