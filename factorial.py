def factorial(n):
   
    if n == 1:
        return 1
    
    return n * factorial(n-1)


print(factorial(4))



def fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(4))