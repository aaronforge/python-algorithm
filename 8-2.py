d = { 1: 1, 2: 1 }

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if x in d:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)

    return d[x]


print(fibo(99))