# def citeste_stud(cale_fisier):
#     rezultat = []
#     with open(cale_fisier) as f:
#         for linie in f.readlines():
#             linie = linie.strip()
#             nume, grupa, *note = linie.split(",")

#             # Varianta 1
#             # note = list(map(int, note))

#             # Varianta 2
#             # note_int = []
#             # for nota in note:
#             #     note_int.append(int(nota))

#             # Varianta 3
#             for i in range(len(note)):
#                 note[i] = int(note[i])

#             rezultat.append((nume, grupa, note))
#     return rezultat

# stud = citeste_stud("studenti.csv")
# # print(stud)
# # for s in stud:
# #     print(s)

# # # def plus1(x):
# # #     return x + 1

# # # nr = [1, 2, 3]
# # # print(list(map(plus1, nr)))

# # L = [1, 2, 1, 1, 10000000]
# # lista_de_frecventa = {}
# # for nr in L:
# #     if nr not in lista_de_frecventa:
# #         lista_de_frecventa[nr] = 0

# #     lista_de_frecventa[nr] = lista_de_frecventa[nr] + 1

# # print(lista_de_frecventa)

# # print(L)

# # d = {}
# # # L = [1, 2]
# # # d[tuple(L)] = "Ana"
# # # print(d)

# # d = {
# #     "altdictionar": {
# #         1: [1, 2, 3]
# #     }
# # }

# # print(d)
# # print(d["altdictionar"])

# # for i in range(5):
# #     if i==1:
# #         print(i)
# #         break
# # else:
# #     print("A iesit normal")

# def verifica_picat(lista_tupluri):
#     l_rezultat=[]
#     for tuplu in lista_tupluri:
#         s=0
#         trecut = False

#         for elem in tuplu[2]: #din note
#             s+=elem
#             if elem == 0:
#                 break
#         else:
#             trecut = True
        
#         l_rezultat.append((tuplu[0], tuplu[1], tuplu[2], trecut))
    
#     return l_rezultat

# print(verifica_picat(stud))
        
l=[3,1,2,6,9,4,3,1]
l.sort(key=lambda x: x)

print(l)

def patrat(x):
    return x ** 2

patrate = list(map(lambda x: x**2, l))
print(patrate)