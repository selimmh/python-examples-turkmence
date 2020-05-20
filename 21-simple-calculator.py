# Bu programma ýönekeý kalkulýator

flag = False
while True:
    print('''\nAmal saýlaň
        [N] Sanlary giriziň
        [+] Goşmak
        [-] Aýyrmak
        [*] Köpeltmek
        [/] Bölmek
        [X] Çykalga ''')

    choice = input("\nSiziň saýlawyňyz: ")
    if choice.upper() == 'N':
        num1 = float(input("Birinji sany giriziň: "))
        num2 = float(input("Ikinji sany giriziň: "))
        input()
        flag = True

    elif choice == '+' and flag == True:
        print(num1, "+", num2, "=", num1 + num2)
        input()

    elif choice == '-' and flag == True:
        print(num1, "-", num2, "=", num1 - num2)
        input()

    elif choice == '*' and flag == True:
        print(num1, "*", num2, "=", num1 * num2)
        input()

    elif choice == '/' and flag == True:
        print(num1, "/", num2, "=", num1 / num2)
        input()

    elif choice.upper() == 'X':
        print("Programmadan çykylýar...")
        break 

    elif flag == False:
        if choice in ('+', '-', '*', '/'):
            print("Sanlar girizilmedi")
            input()
        else:
            print("Beýle saýlaw ýok")
            input()

    else:
        print("Beýle amal ýok")
        input()