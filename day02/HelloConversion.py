import math as m

#資料的轉換
chinese = "90"
math = "80"
english = "100"

sum = chinese + math + english # [+] 對於字串而言是連接符號
print("sum = ", sum )

print(type(chinese), type(math), type(english))
sum2 = int(chinese) + int(math) + int(english)
print("sum2 = ", sum2)

# 資料的轉換(LAB)
# 求 BMI 取到小數點2位
h, w = "180.5", "85"
h = float(h)
w = float(w)
bmi = w / (h/100)**2
bmi = w / m.pow(h/100, 2)
print(bmi, bmi)
print("%.2f" % bmi )
