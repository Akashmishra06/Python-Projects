# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.


for pr in range(1, 11):
    if pr == 5:
        continue
    print(f"3 * {pr} = ", 3 * pr)