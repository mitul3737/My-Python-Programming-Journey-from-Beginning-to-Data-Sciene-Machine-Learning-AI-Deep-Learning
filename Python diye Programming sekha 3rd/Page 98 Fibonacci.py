def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)
n=int(input("Give the number to check for Fibonacci: \n"))
print(n," no Fibonacci number is ",fibonacci(n))