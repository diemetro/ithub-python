import random
print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
a=input()
counter=0
while counter!=2:
    if a.isupper():
        if a=="ПОКА!":
            counter+=1
        else:
            counter=0
        print("НЕТ, НИ РАЗУ С 19"+str(random.randint(31, 49))+" ГОДА!")
        a=input()
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
        counter=0
        a=input()
print("ДО СВИДАНИЯ, МИЛЫЙ!")