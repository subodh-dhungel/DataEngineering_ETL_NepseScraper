def fibonacciGenerator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = fibonacciGenerator(20)

for num in fib:
    print(num)