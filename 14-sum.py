# Bu programma, berlen sana çenli bitin sanlaryň jemini hasaplaýar

num = int(input("San giriz: "))
my_list = []

if num < 0:
    print("Positiv san giriz")

else:
    for i in range(0,num):
        my_list.append(i)

print(my_list)
print(sum(my_list))
    
    