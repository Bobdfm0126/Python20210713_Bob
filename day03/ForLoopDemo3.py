# 99 乘法表
# 雙重迴圈


for x in range(1, 10):
    for y in range(1, 10):
        sum = x*y
        print("%d x %d = %d" % (x, y, sum), end ="\t")
    print()