# program to find fibonacci sequence of particula range:

a=int(input("enter the number:"))
def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)
for i in range(a):
    print (fibonacci(i))
