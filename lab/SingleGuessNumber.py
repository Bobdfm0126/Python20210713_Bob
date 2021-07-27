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

ps:
最多猜7次， 若超過則程式自動結束(while)
'''
import random

ans = random.randint(1, 99)
min, max = 0, 100
max_amount = 7
cur_amount = 0

while True:
    # 次數 + 1
    cur_amount = cur_amount + 1
    if cur_amount > max_amount:
        print('次數用完，程式結束。答案:%d' % ans)
        break

    # User 猜 (最多猜7次)
    guess = input('請在%d~%d 間猜一個數字:' % (min, max))
    guess = int(guess) # 字串轉數字
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