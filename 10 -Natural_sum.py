# # Program to find the sum of natural numbers up to n

# n = int(input("Enter a number: "))
# sum_n = n * (n + 1) / 2
# print(f"Sum of natural numbers up to {n} is {sum_n}")


# another method to find sum of natural num:

n=(int(input("enter the number:")))
sum=0
for i in range(1,n+1):
    if n>0:
        sum += i 
print(sum)
