# Bu programma berlen X we Y niň kwadrantyny tapýar

x = int(input("X giriz: "))
y = int(input("Y giriz: "))

if x > 0 and y > 0:
    print("\nX we Y, 1-nji Kwadrantda ýerleşýär")

elif x < 0 and y > 0:
    print("\nX we Y, 2-nji Kwadrantda ýerleşýär")

elif x < 0 and y < 0:
    print("\nX we Y, 3-nji Kwadrantda ýerleşýär")

elif x > 0 and y < 0:
    print("\nX we Y, 4-nji Kwadrantda ýerleşýär")

else:
    print("\nX we Y esasda")

print("X = {} | Y = {}".format(x,y))