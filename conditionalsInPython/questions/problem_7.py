# Question_7

# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

import random

while True:

    coffee_order = random.choice(["Small", "Medium", "Large"])
    print(coffee_order)

    if coffee_order == "Small":
        print("if u want to add extra shot in small(Enter Capital(Y)): ")
        checkExtraShot = input("pls Enter(Y/N): ")
        if checkExtraShot == "Y":
            print("*" * 70)
            print("Small with extra shot is ordered")
            print("*" * 70)
        else:
            print("*" * 70)
            print("Small coffee is order pls wait")
            print("*" * 70)
        

    if coffee_order == "Medium":

        print("if u want to add extra shot in small(Enter Capital(Y)): ")
        checkExtraShot = input("pls Enter(Y/N): ")
        if checkExtraShot == "Y":
            print("*" * 70)
            print("Medium with extra shot is ordered")
            print("*" * 70)
        else:
            print("*" * 70)
            print("Medium coffee is order pls wait")
            print("*" * 70)
        

    if coffee_order == "Large":

        print("if u want to add extra shot in small(Enter Capital(Y)): ")
        checkExtraShot = input("pls Enter(Y/N): ")
        if checkExtraShot == "Y":
            print("*" * 70)
            print("Large with extra shot is ordered")
            print("*" * 70)
        else:
            print("*" * 70)
            print("Large coffee is order pls wait")
            print("*" * 70)