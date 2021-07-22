# 買飲料程式
# 飲料一瓶 10 元
# 買二送一
# 問: 若有 100 元， 可買幾瓶飲料 ?

if __name__ == '__main__':
    price = 10  # 飲料一瓶 10 元
    balance = 100  # 皮包內有 100 元

    amount = int(balance/price)
    bonus = int(amount/2)
    amount = amount + bonus
    print(amount)

    '''
    balance/price = 11
    int(11/2) = 5
    00 00 00 00 00 0
     0  0  0  0  0
    '''