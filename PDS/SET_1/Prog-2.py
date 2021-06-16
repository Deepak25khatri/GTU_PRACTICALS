def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=int(input("Enter the number : "))
fib=fibonacci(n)
print("The",n,"th number in fibonacci series is",fib)