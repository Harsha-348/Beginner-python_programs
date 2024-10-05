#program to print prime numbers using python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 250):
    if is_prime(num):
        print(num, end=" ")