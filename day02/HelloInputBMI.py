# 撰寫一個 BMI 系統
# 可以輸入人名, 身高cm, 體重kg
# 系統會算出 BMI 的結果與是否是正常, 過低(<=18), 過高(>23)
# 資料格式呈現 : ___的身高是 ___cm 體重是 __ kg BMI 計算結果為 __.__ (____)
# 資料範例呈現 : 小明的身高是 170cm 體重是 60 kg BMI 計算結果為 20.76 (正常)
from random import random

if __name__ == '__main__':
    name = input('請輸入姓名:')
    h = input('請輸入身高(公分):')
    w = input('請輸入體重(公斤):')
    h = float(h)
    w = float(w)
    bmi = w / (h / 100) ** 2
    result = "正常"
    if  bmi <= 18 :
        print("過低")
    elif bmi > 23  :
        print("過高")
    print("%s的身高是%.1fcm 體重是%.1fkg BMI 計算結果為%.2f(%s)") %





