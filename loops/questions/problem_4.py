# 4. Reverse a String
# Problem: Reverse a string using a loop.


str = "Akash Mishra"
rever_str = ""
# print(str[::-1])

for char in str:
    rever_str = char + rever_str

print(rever_str)