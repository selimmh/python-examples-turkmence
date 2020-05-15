# Bu programma ulanyjydan üçburçlygyň taraplarynyň bahasyny alýar we onuň perimeter we meýdanyny tapýar
# Perimeter: a+b+c | Meýdan: √(s(s-a)*(s-b)*(s-c)), s = (a+b+c)/2

a = int(input("1-nji tarap: "))
b = int(input("2-nji tarap: "))
c = int(input("3-nji tarap: "))

per = a+b+c
print("Perimeter:",per)

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Meýdan:",area)