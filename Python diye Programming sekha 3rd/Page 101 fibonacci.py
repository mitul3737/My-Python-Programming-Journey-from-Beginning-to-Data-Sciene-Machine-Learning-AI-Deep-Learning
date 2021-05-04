def fibonacci(n):
    print("Trying to find fibonacci for",n)
    if n==1 or n==2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

if __name__=="__main__":
    x=int(input("Check with a number"))
    print(x,"th fibonacci number is ", fibonacci(x))