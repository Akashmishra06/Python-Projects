x = ("conection", "lemon", "ginger")

y = enumerate(x)

print(list(y))
print(y)

file = open('text.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close


with open('youtube.txt', 'w') as file:
    file.write('youtube')