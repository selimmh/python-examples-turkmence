# Bu programma kwadrat deňleme çözýär
# ax^2 + bx + c = 0 | a,b,c e R | a ≠ 0

import cmath

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# diskriminant
d = (b**2) - (4*a*c)

# jogaplar
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("Jogap 1:", sol1)
print("jogap 2:", sol2)