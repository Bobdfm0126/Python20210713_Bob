if __name__ == '__main__':
    sum = int(input('請輸入雞+兔的總數'))
    # 奇數，負數 ...... 都會造成錯誤
    # 檢查 sum 是否為奇數或負數
    # 作業...
    min, max = sum * 2, sum * 4
    feet = int(input('請輸入雞的腳+兔的腳的總數( %d ~ %d):' % (min, max)))

    # 檢查 腳 是否在 min, max 間
    if(min <= feet <= max):
        rabbit = (feet - sum * 2)/2
        chicken = sum - rabbit
        print("雞:%d 兔:%d" % (chicken, rabbit))
    else:
        print('輸入錯誤')