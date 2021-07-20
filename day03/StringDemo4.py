word = '''
        國文:100
        數學:80
        英文:90
       '''
# 提示斷行 = \n

array = word.spilt('\n')
print(array, len(array))
print('array[1] 沒有去除左右空白:', array[1])
print('array[1] 有去除左右空白:', array[1].strip)

chinese = array[1].strip().spilt(":")[1]  # strip() 去除兩邊空白
math = array[1].strip().spilt(":")[1]  # strip() 去除兩邊空白
english = array[1].strip().spilt(":")[1]  # strip() 去除兩邊空白
sum = int(chinese) + int(math) + int(english)
print("總分: %d" % sum)
