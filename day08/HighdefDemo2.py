# 加10%
def addTen(x):
    return x * 1.1

# 減10%
def subTen(x):
    return x * 0.9

# 減1%
def subOne(x):
    return x * 0.99

# 加1%
def addOne(x):
    return x * 1.01

def calc(func1, func2, x):
    if x >= 90:
        return func1(x) + func1(x)
    elif x >= 60:
        return func1(x)
    else:
        return func2(x)

if __name__ == '__main__':
    # 分數 >= 60 加10% 反之 減10%
    x = 75
    print(calc(addTen, subTen, x))
    x = 45
    print(calc(addOne, subTen, x))
    #-----------------------------
    x = 75
    print(calc(addTen, subOne, x))
    x = 45
    print(calc(addOne, subOne, x))
