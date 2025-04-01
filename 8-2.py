memo = { 0: 0, 1: 1 }

def fibo(x: int):
    if x in memo:
        return memo[x]
    
    print(f'f({x})')
    
    memo[x] = fibo(x - 2) + fibo(x - 1)

    return memo[x]

print(fibo(9))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(10))