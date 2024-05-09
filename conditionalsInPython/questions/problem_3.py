# Question_3

# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

while True:

    marks = int(input("Enter the value of marks: "))

    if marks < 101:        
        if marks > 89:
            print("A")
        elif marks > 79:
            print("B")
        elif marks > 69:
            print("C")
        elif marks > 59:
            print("D")
        elif marks < 60:
            print("F")