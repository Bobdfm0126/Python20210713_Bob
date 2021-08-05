# 每次呼叫可 +10 分
def addTen():
    global score
    score = score + 10

if __name__ == '__main__':
    score = 50
    print('score=', score)  # 50
    addTen()
    print('score=', score)  # 60
    addTen()
    addTen()
    addTen()
    print('score=', score)  # 90