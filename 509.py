def func(x):
    if x == 0: return 0
    fib = [1] * x
    i = 2
    while i <= x - 1:
        fib[i] = fib[i - 1] + fib[i - 2]
        i += 1
    return fib[-1]


print(func(2))
