'''
迴圈 for-in 、while
for 變數 in range串列:
    程式區塊
'''

for x in range(10): #(0~9) 10個
    print(x, end=", ")
print("\n----------")

for x in range(1, 11): #(1~10) 10個
    print(x, end=", ")
print("\n----------")

for x in range(1, 11, 2):  # (1~10) 間隔2
    print(x, end=", ")
print("\n----------")

# break 跳出迴圈
# continue 直接跳入下個迴圈

for x in range(1, 11): #(1~10) 10個
    # x 資料大於 5 則迴圈停止
    if x > 5 :
        print('離開迴圈, x=', x)
        break:
    print("x=", x)
print("----------")

for x in range(1, 11):
    # 遇到偶數則立即進行下一次迴圈
    if x % 2 == 0:
        continue

