x = input('Enter a number to see its multiplication table: ')
x = int(x)

for y in range(1, 11):
    z = x * y
    print(x, '*', y, '=', z)