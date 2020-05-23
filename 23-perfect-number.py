# Bu programma sanyň ajaýypdygyny ýa-da däldigini hasaplaýar
# Ajaýyp san (perfect number) - bu bölüjileriň jemine deň bolan positive bitin san
# Käbir ajaýyp sanlar: 6, 28, 496, 8128, 33550336, 8589869056, 137438691328

def perfect_num():
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i 

    if sum == num:
        print(num, "bu ajaýyp san")
    else:
        print(num, "bu ajaýyp san däl")

num = int(input("San giriz: "))
perfect_num()