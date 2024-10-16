# Program to calculate compound interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
compoundings_per_year = int(input("Enter number of times interest is compounded per year: "))

compound_interest = principal * (1 + rate / (compoundings_per_year * 100)) ** (compoundings_per_year * time)
print(f"Compound Interest is {compound_interest - principal}")
