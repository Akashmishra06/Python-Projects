# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 10
sumOfPositiveNumber = 0

for num in range(1, n+1):
    if num % 2 == 0:
        sumOfPositiveNumber = sumOfPositiveNumber + num

print(sumOfPositiveNumber)