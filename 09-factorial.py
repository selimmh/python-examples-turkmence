# Bu programma n faktoriýal hasaplaýar

num = int(input("San giriz: "))

fact = 1
for i in range(1,num+1):
    fact = fact * i

print(fact)