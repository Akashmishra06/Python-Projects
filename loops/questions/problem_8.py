# 8. Prime Number Checker
# Problem: Check if a number is prime.

inputTheNumber = int(input("Enter the Number: "))

is_prime = True

if inputTheNumber > 1:
    for i in range(2, inputTheNumber):
        if (inputTheNumber % i) == 0:
            is_prime = False
            break


print(is_prime)