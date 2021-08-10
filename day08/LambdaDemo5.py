id = 'A123456789'
sex = id[1]  # 1: 男生, 2: 女生

printSex = {  # dict 結構
    "1": lambda n: print("男生", n),
    "2": lambda n: print("女生", n)
}

printSex.get(sex)()  # 最後要加上()， 因為是函式

SexObj = printSex.get(sex)
SexObj()