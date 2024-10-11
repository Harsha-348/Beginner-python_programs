# Program to find a factorial of a number:
#factorial(n)= factorial(n) * factorial(n-1)

def factorial(n):
    for i in range(n+1):
        if n==0 or n==1:
            return 1
        else:
            return n * factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

