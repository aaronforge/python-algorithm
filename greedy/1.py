def get_coin_count(n: int):
    print('=====')
    print(n, '원')

    coin_types = [500, 100, 50, 10]

    count = 0

    for coin in coin_types:
        # 현재 화폐로 거슬러줄 수 있는 동전 수
        count += n // coin

        # 현재 화폐로 나눈 뒤 나머지
        n %= coin

    print(count, '개')

    
    return count


# 500-2, 100-2, 50-1, 10-1 => 6
get_coin_count(1260)

# 500-2, 100-3, 50-1, 10-1 => 7
get_coin_count(1360)

# 500-5, 100-3, 50-1, 10-0 => 9
get_coin_count(2850)


# 500-0, 100-0, 50-1, 10-1 => 2
get_coin_count(60)