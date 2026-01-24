# def citire_numere(nume_fisier):
#     f=open(nume_fisier,"r")
#     L=[]
#     for linie in f:
#         linie=linie.strip()
#         l=[]
#         for element in linie.split():
#             l.append(int(element))
#         L.append(l)
#
#     return L
# #print(citire_numere("12.12.txt"))
#
#
# def prelucrare_lista(liste):
#
#     minlenx = float("inf")
#
#     for i,x in enumerate(liste):
#
#
#         minx = min(x)
#         while(minx in x):
#              liste[i].remove(minx)
#
#
#
#         minlenx=min(minlenx, len(x))
#
#     for i,x in enumerate(liste):
#         liste[i] = x[:minlenx]
#         #x[start : stop : step]
#
#
# #print(prelucrare_lista(citire_numere("12.12.txt")))
# L=citire_numere("12.12.txt")
# l=citire_numere("12.12.txt")
# prelucrare_lista(l)
# for linie in l:
#     print(*linie)
#
# k=int(input("k = "))
# f = open("cifre.out","w")
# def are_k_cifre(x,k):
#     x=str(x)
#     if len(x)==k:
#         return True
#     else:
#         return False
# L1=[]
# for linie in L:
#     for element in linie:
#         if are_k_cifre(element,k)==True:
#
#             L1.append(element)
#
# multime = set(L1)
# l1=list(multime)
# l1.sort(reverse=True)
# for element in l1:
#     f.write(f"{element} ")
#
# ex2
from plistlib import dumps


def citireCinema(path):

    toate_orele = {}

    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:

            cinema, film , ora = line.strip().split(' % ')

            if not cinema in toate_orele:
                toate_orele[cinema] = {}
            if film not in toate_orele[cinema]:
                toate_orele[cinema][film] = set()

            for h in ora.split():
                toate_orele[cinema][film].add(h)
    return toate_orele


d=citireCinema("cinema.in")

def sterge_ore(d,cinema,film,ore):
    for i in ore:
        d[cinema][film].discard(i)
    return list(d[cinema][film])

print(sterge_ore(d,"Cinema 1","Minionii 2",set(["12:30"])))


















