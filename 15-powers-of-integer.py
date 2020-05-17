# Bu programma, bir sanyň berlen sana çenli ähli derejelerini tapýar

num = int(input("San: "))
terms = int(input("Dereje: "))

answer = list(map(lambda x: num ** x, range(terms)))

for i in range(terms):
   print(num,"^",i,"=",answer[i])