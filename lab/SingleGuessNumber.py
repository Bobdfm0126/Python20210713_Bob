'''
由系統產生 1~99 之間的亂數
令 ans = 77
    min ~  max
=> 請在 0 ~ 100 之間猜一個數字
使用者猜 50
=> 請在 50 ~ 100 之間猜一個數字
使用者猜 90
=> 請在 50 ~ 90 之間猜一個數字
'''
'''
使用者猜 77
對了 !
'''
import random

ans = random.randint(1, 99)
min, max = 0, 100

while True:
    # User 猜
    guess = input('請在%d~%d 間猜一個數字:' % (min, max))
    guess = int(guess) #字串轉數字
    # 驗證範圍 ?
    if (guess <= min or guess >= max):
        print('範圍錯誤, 請重新輸入 !')
        continue
    # 判斷是否答對 ?
    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('答對了')
        break  # 迴圈結束