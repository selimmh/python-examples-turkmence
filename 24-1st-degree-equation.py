# Bu programma 1nji derejeli deňlemäni çözýär

print ("Deňleme - A + B*X = C\n")
a=int(input("A-ny giriz: "))
b=int(input("B-ny giriz: "))
c=int(input("C-ny giriz: "))

if b == 0:
  print("Deňleme 1-nji derejeli däl")

else: 
    x=(c-a)/b
    print ("X-iň bahasy: " + str(x))