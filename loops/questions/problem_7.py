# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    inpu = int(input("Enter the value of inpuuu: "))
    if inpu in range(1,11):
        print("input is correct")