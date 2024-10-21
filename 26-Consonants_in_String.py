# Program to count consonants in a string
string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for char in string:
    if char.isalpha() and char not in vowels:
        count += 1
print(f"Number of consonants in the string is {count}")

'''
This program counts the number of consonants in a 
string by iterating through each character.
'''
