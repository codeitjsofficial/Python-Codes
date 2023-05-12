def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Enter the number of Fibonacci numbers you want to print:")
n = int(input())

print("The first {} Fibonacci numbers are:".format(n))
for i in range(n):
    print(fibonacci(i))
