def solution(money):
    money = money
    answer = 0
    coins = [500, 100, 50, 10]

    for coin in coins:
        answer += money // coin
        money = money % coin

    return answer


print(solution(1230))  # ==> 2+2+3 = 7
print(solution(1320))  # ==> 2+3+2 = 7
