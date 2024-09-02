def fibonacci():
    n1=0
    n2=1
    while True:
        yield n1
        n1,n2=n2,n1+n2

n=int(input('enter a number'))
print("Number of first ",n,"Fibonacci numbers:")
fib = fibonacci()
for _ in range(n):
    print(next(fib),end=" ")