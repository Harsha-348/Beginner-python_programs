# Program to find LCM of two numbers
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm_value = lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {lcm_value}")

'''Explanation: This program calculates the least common 
multiple (LCM) using the formula `abs(a*b) // gcd(a, b)'''
