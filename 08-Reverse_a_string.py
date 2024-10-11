# Python Program to reverse a string:

n=(input("enter a charcter:"))
rev=n[::-1]
print(rev)

# # Python Program to reverse a integer:
n=int(input("enter the number:"))
rev=0

while n>0:
    ld= n % 10

    rev=(rev*10)+ld

    n=n//10
print(rev)


