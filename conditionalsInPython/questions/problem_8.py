# Question_8

# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).\


password = input("Pls Enter Your Password: ")
chars_in_Password = len(password)


if chars_in_Password < 6:
    print("Weak")

if chars_in_Password < 11:
    print("Medium")

if chars_in_Password > 10:
    print("Strong")