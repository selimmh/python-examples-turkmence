# Bu programma ulanyjydan üçburçlygyň taraplarynyň bahasyny alýar we onuň perimeter we meýdanyny tapýar
# Perimeter: a+b+c | Meýdan: √(s(s-a)*(s-b)*(s-c)), s = (a+b+c)/2

a = float(input("1st side: "))
b = float(input("2nd side: "))
c = float(input("3rd side: "))

per = a+b+c
print("Perimeter is:",per)

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area is: %0.2f" %area)