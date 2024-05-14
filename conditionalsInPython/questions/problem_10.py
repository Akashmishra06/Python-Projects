# Question_10

# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

import random

pets_species = random.choice(["Dog", "Cat"])
pets_age = int(input("Enter the value of pets_age(in Years): "))


if pets_species == "Dog":
    if pets_age < 2:
        print("Puppy food")
    else:
        print("give anything")

if pets_species == "Cat":
    if pets_age > 5:
        print("Senior cat food")
    else:
        print("give kitten food")