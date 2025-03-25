# 5 8 3 => 배열 크기 N, 숫자 더해지는 횟수 M, 반복 가능 최대 수 K
# 2 4 5 4 6 => N 개의 자연수

def get_result():
    n, m, k = map(int, '5 8 3'.split(' '))
    data = list(map(int, '2 4 5 4 6'.split(' ')))
    data.sort()

    result = 0

    first = data[-1]
    second = data[-2]

    result_list = []

    while m > 0:
        for i in range(k):
            result += first
            result_list.append(first)

            m -= 1
        
        result += second
        result_list.append(second)
        
        m -= 1
    
    print(result_list, result)

def get_result():
    n, m, k = map(int, '5 8 3'.split(' '))
    data = list(map(int, '2 4 5 4 6'.split(' ')))
    data.sort()

    first = data[-1]
    second = data[-2]

    # 6 6 6 5 / 6 6 6 5
    # => 반복 수열의 길이: k + 1
    # => 수열의 반복 횟수: m / (k + 1)
    # => 가장 큰 수의 등장 횟수 = 수열의 반복 횟수 * k
    # => (m / (k + 1)) * k * 가장 큰 수
    # => 위의 경우에서 반복 휫수가 나누어 떨어지지 않는 경우를 더해야 함
    # => int((m / (k + 1)) * k) + (m % ( k + 1 ))

    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = first * count
    result += (m - count) * second


get_result()