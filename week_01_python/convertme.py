def factorial(n):
    prod = 1
    for i in range(n,1,-1):
        prod = prod * i
    return prod

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print("Good News Everyone!")
print(f"1! = {factorial(1)}" )
print(f"fib(1) = {fib(1)}" )
