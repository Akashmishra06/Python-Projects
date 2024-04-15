# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.


num = int(input("Enter a number to calculate its factorial: "))
factrial = 1
while num > 0:
    factrial *= num
    num -= 1

print(factrial)