# Question_1

# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

while True:

    age = int(input("Enter the value of age: "))

    if age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 60:
        print("Adult")
    elif age > 60:
        print("Senior")