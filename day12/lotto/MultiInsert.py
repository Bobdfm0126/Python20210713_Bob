import sqlite3
import random

conn = sqlite3.connect('lotto.db')
cursor = conn.cursor()

lottos = []

for i in range(10000):
    # 1~49 不重複數字
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 49))

        # 加入到 lottos
        lottos.append(nums)

print(len(lottos), lottos)