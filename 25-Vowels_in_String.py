# Program to count vowels in a string
string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"Number of vowels in the string is {count}")

'''This program counts the number of vowels 
in a string by iterating through each character'''
