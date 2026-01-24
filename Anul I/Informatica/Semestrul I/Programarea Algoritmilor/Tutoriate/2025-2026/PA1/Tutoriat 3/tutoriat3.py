# materii = ["Algebra", "Analiza", "Fizica"]
#
# # Adăugare
# materii.append("Programare")  # ["Algebra", "Analiza", "Fizica", "Programare"]
#
# # Modificare
# materii[1] = "Analiza Matematică"  # ["Algebra", "Analiza Matematică", "Fizica", "Programare"]
#
# # Ștergere după valoare
# materii.remove("Fizica")  # ["Algebra", "Analiza Matematică", "Programare"]
#
#
# print(materii)
#
# # Ștergere după index și returnare
# materii.pop(1)  # ["Analiza Matematică", "Programare"]
#
# print(materii)  # Ieșire: ['Analiza Matematică', 'Programare']

#1
# lista = [ int(x) for x in input().split()]
# print(lista)

#4
# cuvinte = input().split()
# n = int(input())
# cuvinte_filtr = [cuv for cuv in cuvinte if len(cuv)<n]
# #print(cuvinte_filtr)

#cuv = [cuv for cuv in input.split() if len(cuv) < 5]
#5
# lista = input.split()
# lista2 = [cuv.upper() for cuv in lista]
# print(lista2)

#6
# with open("note.txt") as f:
#     elevi_eminenti = [linie.split()[0] for linie in f if int(linie.split()[1]) >=9]
#
# print(elevi_eminenti)

#7
# lista = [int(x) for x in input() if x.isdigit()]
# print(lista)

#8
# import math
# lista = [int(x) for x in input().split(',')]
# lista2 = [x**(1/2) for x in lista if x%4 == 0]
# print(lista2)

#9
# lista = ["mar","banana","caisa"]
# for i,fruct in enumerate(lista):
#     print(i,fruct)

# orase = input().split()
# # orase_nou = [ oras for i,oras in enumerate(input().split()) if i%2==0 and len(oras)>5 ]
#
# orase_nou=[oras for oras in orase[::2] if len(oras)>5]
# print(orase_nou)

# n = int(input())
# matrice = [[i*j for i in range(n)] for j in range(n)]
#
# for linie in matrice:
#     print(linie)

# n = int(input())
# matrice = []
# for i in range(n):
#     linie = input().split()
#     matrice.append(linie)
#
# lista_poz = [ int(x) for linie in matrice for x in linie if int(x)>0]
# print(lista_poz)

#12
# n = int(input())
# matrice = []
# for i in range(n):
#     linie = input().strip().split()
#     linie2=[int(x) for x in linie]
#
#     matrice.append(linie2)
#
# sume = [sum(lista) for lista in matrice]
# print(sume)
#print("6      nananan            6666".strip('6'))






