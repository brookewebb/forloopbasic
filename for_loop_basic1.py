print('This is 0-150!')
for x in range(151):
    print(x)


print('These are the multiples of 5!')
for x in range(1001):
    if x % 5 == 0:
        print(x)

print('Counting Dojos')
for x in range(101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

print('Wow, a super large number! Scary!')
sum = 0 
for x in range(500001):
    if x % 2 == 0:
        sum = sum + x
print(sum)

print('Counting down by Fours')
for x in range(2018, 0, -4):
    print(x)
    
print('Hey, I made this one!')
for x in range(0, 100, 5):
    print(x)