def fibonacci_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(1000):
        print(next(fib_gen)) # Output: 0, 1, 1, 2, 3