# 10點半對戰
# 今天你有 100 元
# 可以自由下注
import day04.PokerDemo5 as poker

if __name__ == '__main__':
    balance = 100
    while True:
        print('balance:', balance)
        bet = int(input('請下注(0:離開): '))

        if bet == 0 and balance == 0:
            break;

        result = poker.playGame()
        print(result)
        balance = balance + (result * bet)
        print(balance)