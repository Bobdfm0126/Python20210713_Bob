# 判斷 x 是否為質數
# 只能被 1 與自己整除
# x = 5
# 2, 3, 4
isPrime = True
x = 13
isPrime = True
for i in range(2, int(x/2+1)):
    if x % i == 0:
        isprime = False
        break

print("%d 是否是質數: %s" % (x, isPrime))