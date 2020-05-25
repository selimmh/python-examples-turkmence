# Bu programma list elementlerini ulanyjydan alýar we onuň iň uly elementini print edýär

n = int(input("Listiň uzynlygy: "))
list = [0]*n

for i in range(n):
    a = int(input("Element ["+str(i+1)+"]: "))
    list[i] = a

print("\nIň uly element: ", max(list))