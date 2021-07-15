import random as r

a = r.randint(1, 3) # 1-3
print("a =", a)

b = r.randrange(2, 10, 2) #2~9 之間取出 (2, 4, 6, 8) -> 隨機
print("b =", b)

# 樂透電腦選號
# 四星彩 4 個 0~9 的組合，數字可重複
n1 = r.randint(0, 9)
n2 = r.randint(0, 9)
n3 = r.randint(0, 9)
n4 = r.randint(0, 9)
print(n1, n2, n3, n4)