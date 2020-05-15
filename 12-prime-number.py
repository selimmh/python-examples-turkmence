# Bu programma berlen sanyň ýönekeý ýa-da däldigini barlaýar (prime number)

num = int(input("San giriz: "))

if num > 1:
   for i in range(2,num):
        if (num % i) == 0:
           print("Ýönekeý däl")
           break
        else:
            print("Ýönekeý")
            break

else:
   print("Ýönekeý däl, n < 1")