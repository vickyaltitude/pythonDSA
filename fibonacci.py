def fibonacci(n):
    my_fib_list = [0,1,1,2]

    if n <= 3:
        return my_fib_list[n]

    for x in range(4,n+1):
        my_fib_list.append(my_fib_list[x-1] + my_fib_list[x-2])
    
    return my_fib_list[n]


print(fibonacci(8))