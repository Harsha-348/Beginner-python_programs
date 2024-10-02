
# Program to print even numbers from 1 to 200:
for num in range(1,200+1):
        if num % 2 ==0:
            print(num,end=" ")
    
''' `for` loop iterates from 1 to 100,
 and the `if` statement checks if the number is even.'''

print(''' 
''')
#check whether the number is even or not:
num=int(input("enter the number:"))

if num % 2==0 :
      print(f"the entered number - {num} is an even number")
else:
      print(f"the entered number - {num} is not an even number")

