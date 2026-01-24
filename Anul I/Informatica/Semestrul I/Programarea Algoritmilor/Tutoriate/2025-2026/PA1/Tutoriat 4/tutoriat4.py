# zile=("luni","marti","mircuri","joi","vineri")
# print(zile[1:4])
from sys import prefix

# a,*c=(1,2,3)
# print(a)
#
# print(c)

# litere_10=[chr(x) for x in range(ord('a'),ord('l'))]
# print(litere_10)

# m=[[1,2,3],[4,5,6],[7,8,9]]
# numere=[m[i][i]*m[i][i] for i in range(len(m))]
# print(numere)

#numere=[i for i in range(10, 100) if i%7!=0 and i**(1/2)*i**(1/2)!=i]
#print(numere)



# print([x for x in range(100,1000) if str(x)[0]<str(x)[1]<str(x)[2]])

#lista_numere=[800,246,153,12]
#prefix_s=[i for i in lista_numere if i%5!=0 and len([x for x in str(i)[::-1] if x == '5' or x == '0']) == 0]
#print(prefix_s)


elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
nume = "Mihai"
ok=False

# rez=[i for i in elevi if i[1]>8]
#
# print(rez)

# for i in elevi:
#     if i[0]==nume:
#         ok=True
#         break;
#
# print(ok)
# med=0
# for i in elevi:
#     med+=i[1]
# med/=len(elevi)
# print( med)

# elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
# v=min(elevi,key=lambda x:x[1])
# print(v)


# note = [("Ana", 10), ("Ion", 8), ("Ana", 10)]
#
# duplicates=list(set(note))
#
# print(duplicates)
#
# reversedTuple=[x[::-1] for x in elevi]
# print(reversedTuple)

#Problema 17
# lista = []
# with open("note2.txt") as f:
#     for linie in f:
#         tuplu = (linie.split()[0], int(linie.split()[1]))
#         lista.append(tuplu)
# print(lista)

numere = [1, 2, 3, 4, 5, 6, 7]

multime={x for x in numere if x%2==1}
print(multime)