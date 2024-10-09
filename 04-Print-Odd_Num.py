
# Program to print odd numbers from 1 to 100
for num in range(1, 200+1):
    if num % 2 != 0:
        print(num,end=" ")

''' The `for` loop iterates from 1 to 100, 
and the `if` statement checks if the number is odd. '''
print('''
      ''')

# Program to check whether the number is odd or not
num=int(input("enter the number:"))

if (num%2)==1 or (num%2)!=0 :
    print(f"The entered number-{num} is an odd number")
else:
    print(f"The entered number-{num} is not an odd number")
