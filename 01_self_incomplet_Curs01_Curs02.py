import random

separator = ("-" * 30)
print(separator)

"""2a. x = 3
print(type(x))
"""
print(separator)

"""2b.x = int(input("Add no."))
print(x, type(x))
"""
print(separator)

x = random.randint(-10, 10)

"""3.. if x > 0:
    print("{} pozitiv".format(x))
elif x == 0:
    print("{} egal cu 0".format(x))
else:
    print("{} negativ".format(x))
"""
print(separator)

"""4.. x = float(input("Insert no."))

if -2 < x < 13:
    print("{} este cuprins in interval".format(x))
else:
    print("{} nu este cuprins in interval".format(x))
"""
print(separator)

"""5. x = int(input("Insert no1."))
y = float(input("Insert no2."))
diferenta = abs(x - y)

if diferenta <5:
    print("Da, este mai mica diferenta decat 5")
elif diferenta==0:
    print("Egala cu 0")
else:
    print("Nu, este mai mare decat 5 diferenta")
"""
print(separator)

"""6.  x=random.randint(-50,50)

if not 5 < x < 27:
    print("In afara intervalului")
else:
    print("In interval")
"""
print(separator)

"""7. x = random.uniform(0.5, 2.5)
y = random.randint(0, 3)

if x > y:
    print("{} este mai mare".format(x))
elif x == y:
    print("{} si {} sunt egale".format(x, y))
else:
    print("{} este mai mare".format(y))
"""

print(separator)

"""8. x = random.randint(1, 5)
y = random.randint(1, 5)
z = random.randint(1, 5)

if x == y == z:
    print("Echilateral")
elif x == y or x == z or y == z:
    print("Isoscel")
else:
    print("Oarecare")"""

print(separator)

"""9a. x = " "

while True:
    x = input("Enter a single character: ")

    if len(x) == 1:
        print(x)
        break
    else:
        print("Enter a single character to continue: ")
        continue"""

print(separator)

"""9b. while True:

    x = input("Insert a letter: ")

    if len(x) == 1 and x in ('a', 'e', 'i', 'o', 'u'):
        print("Vowel")
        break
    elif len(x) == 1 and x not in ('a', 'e', 'i', 'o', 'u'):
        print("Try again, not a vowel")
    elif all(char in ('a', 'e', 'i', 'o', 'u') for char in x):
        print("More than one, but ok!")
        break
    else:
        print("Try again: ")"""

print(separator)

"""10. A, B, C, D, E, F = (9, 10), 8, 7, (6, 5), 4, (0, 1, 2, 3, 4)
print(A, B, C, D, E, F)"""

print(separator)

"""11. x = int(input("Insert a no.: "))

if len(str(x)) == 4:
    print("7895")
else:
    print("10")
"""

print(separator)

"""12. x = int(input("Insert a no.: "))

if len(str(x)) == 6:
    print("6 characters")
else:
    print("Nop")"""

print(separator)

"""13. x = int(input("Insert a no.: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")"""

print(separator)

"""14. x, y, z = int(input("Insert a no.: ")), int(input("Insert a no.: ")), int(input("Insert a no.: "))

if x > y and x > z:
    print("{}, valoarea lui '{}' este cea mai mare".format(x, x))
elif y > x and y > z:
    print("{}, valoarea lui '{}' este cea mai mare".format(y, y))
else:
    print("{}, valoarea lui '{}' este cea mai mare".format(z, z))
"""

print(separator)

"""15a. while True:

    x = int(input("1st value: "))
    y = int(input("2nd value: "))
    z = int(input("3rd value: "))

    if 0 < x < 180 and x + y + z == 180:
        if 0 < y < 180:
            if 0 < z < 180:
                print("Values ok")
                break
            else:
                print("Entry another value for z (0,180): ")
        else:
            print("Entry another value for y (0,180): ")
    else:
        print("Triangle is impossible!")
"""

"""15b.
while True:
    unghiuri = []

    for i in range(3):
        while True:
            valoare_unghi = int(input(f'Introduceti unghiul {i + 1}: '))
            if 0 < valoare_unghi < 180:
                unghiuri.append(valoare_unghi)
                break
            else:
                print('Unghiul trebuie sa fie 0-180. Reintroduceti')
    if sum(unghiuri) == 180:
        print('Unghiurile intruduse sunt: ', unghiuri)
        print('Acestea formeaza un triunghi valid')
        break
    else:
        print('Unghiurile intruduse sunt: ', unghiuri)
        print('Acestea nu formeaza un triunghi valid')"""

print(separator)

"""16. """

print(separator)

"""17. """

print(separator)

"""18.
x = 'Coral is either the stupidest animal or the smartest rock'
y = int(input('Introd un nr: '))
z = x[y:]
print(z)

alpha = x[ :y] + x[-y:]
print(f'Alpha este: {alpha}')

beta = x.split(' ')
beta.pop(-1)
print(beta)


index_start_rock = x.find('rock')
print('index start rock: ', index_start_rock)

string_mic_pana_la_rock = x[:index_start_rock]
print('string pana la rock ', string_mic_pana_la_rock)


index_start_stupidest = x.find('stupidest')
print(index_start_stupidest)

string_pana_la_stupidest = x[:index_start_stupidest]
print(string_pana_la_stupidest)"""

print(ske)

"""19. """

print(separator)

"""20.
a = input('Introd un string: ')
assert a[0].lower == a[-1].lower
print(a)
print("primul si ultimul sunt la fel")"""

print(separator)

"""21. """

print(separator)
