from random import *



def arvud_loendis():
    """Küsib kasutajalt andmeid ja loob seejärel nendest andmetest loendi. Prindib järjestatud, positiivsete, negatiivsete ja nullide loendi. Seejärel arvutab see positiivsete ja negatiivsete elementide keskmise, kuvab need ekraanil ja lisab põhiloendisse.
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=neg=null=[]
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int)->int:
    """Kui a>b siis vahetame neid, siis tagastame need
    :param int a: Arv suurem kui b
    :param int b: Arv suurem kui a
    :rtype: var
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:int,a:int,b:int):
    """Lisab loendisse juhuslikud väärtused a-st b-ni
    :param int n: loenda pikkus
    :param int loend: Loend
    :param int a: Minimaalne number
    :param int b: Maximaalne number
    """
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend:int,p:int,n:int,nol:int):
    """Sirvib numbreid ja leiab positiivse arvu, negatiivse või nulliga võrdse
    :param int loend: Loend
    :param int p: Positiivne number
    :param int n: Negatiivne number
    :param int nol: Null number
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:int)->float:
    """Leidame keskmine, jagades kõigi loendis olevate arvude summa loendis olevate arvude arvuga ja tagastab keskmine
    :param float loend: Loend
    :rtype: var
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:int,el:int):
    """Üksuste loendisse lisamine ja loendi sortimine
    :param int loend: Loend
    :param int el: Element
    """
    loend.append(el)
    loend.sort()

