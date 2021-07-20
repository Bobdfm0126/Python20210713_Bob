# 99 乘法表
# 雙重迴圈
import time

for x in range(1, 10):
    for y in range(1, 10):
        sum = x*y
        print("%d x %d = %d" % (x, y, sum), end ="\t")
        time.sleep(0.2)
    print()