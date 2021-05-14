import calculator as c

num = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

print('choose operator...')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')

pili = int(input('Enter selection: '))

if pili == 1:
    add = c.sum(num,num2)
    print(add)
elif pili == 2:
    sub = c.sub(num,num2)
    print(sub)
elif pili == 3:
    prod = c.prod(num,num2)
    print(prod)
else:
    print('invalid selection')