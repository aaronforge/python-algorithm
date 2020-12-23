# 1230
# 500 500
# 100 100
# 10 10 10

def solution(money):
    money = money
    coins = [500, 100, 50, 10]
    answer = 0

    for coin in coins:
        answer += money // coin
        money %= coin

    return answer


print(solution(1230))
