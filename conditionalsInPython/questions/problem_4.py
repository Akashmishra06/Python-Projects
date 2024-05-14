# Question_4

# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

import random
fruit = "Banana"
colour = random.choice(["Green", "Yellow", "Brown"])

if colour == "Green":
    print("Unripe")
elif colour == "Yellow":
    print("Ripe")
elif colour == "Brown":
    print("Overripe")