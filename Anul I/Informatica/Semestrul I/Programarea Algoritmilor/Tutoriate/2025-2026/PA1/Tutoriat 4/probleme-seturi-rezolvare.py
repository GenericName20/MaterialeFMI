# Probleme cu seturi

# 1.Eliminarea dublurilor
lista = input("Introduceți numere separate prin spațiu: ").split()
lista = [int(x) for x in lista]
print(set(lista))

# 2.Verificarea apartenenței
s = {2, 4, 6, 8, 10}
x = int(input("Introduceți un număr: "))
print(x in s)

# 3.Operații de bază
A = set(map(int, input("Introduceți A: ").split()))
B = set(map(int, input("Introduceți B: ").split()))
print("Reuniune:", A | B)
print("Intersecție:", A & B)
print("Diferență A-B:", A - B)

# 4.Cardinalul unui set
cuvinte = input("Introduceți cuvinte separate prin spațiu: ").split()
print(len(set(cuvinte)))

# 5.Conversie șir în set de caractere
text = input("Introduceți un text: ")
print(set(text))

# 6.Cuvinte comune între două propoziții
p1 = set(input("Propoziția 1: ").split())
p2 = set(input("Propoziția 2: ").split())
print(p1 & p2)

# 7.Cuvinte distincte totale
p1 = set(input("Propoziția 1: ").split())
p2 = set(input("Propoziția 2: ").split())
rez = p1 | p2
print(rez, "Total:", len(rez))

# 8.Diferență simetrică
A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))
print(A ^ B)

# 9.Filtrarea elementelor impare
numere = list(map(int, input("Introduceți numere: ").split()))
print(set(x for x in numere if x % 2 != 0))

# 10.Verificare subset / superset
A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))
print("A subset B:", A <= B)
print("B superset A:", B >= A)

# 11.Intersecția dintre trei seturi
A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))
C = set(map(int, input("Set C: ").split()))
print(A & B & C)

# 12.Caractere comune între două cuvinte
c1 = input("Cuvânt 1: ")
c2 = input("Cuvânt 2: ")
print(set(c1) & set(c2))

# 13.Divizori comuni
a = int(input("a="))
b = int(input("b="))
divs = set(i for i in range(1, min(a,b)+1) if a % i == 0 and b % i == 0)
print(divs)

# 14.Cuvinte unice ignorând majusculele
text = input("Text: ").lower().split()
print(set(text))

# 15.Litere lipsă din alfabet
import string
text = input("Text: ").lower()
print(set(string.ascii_lowercase) - set(text))

# 16.Cuvinte care apar doar într-una din două propoziții
p1 = set(input("Propoziția 1: ").split())
p2 = set(input("Propoziția 2: ").split())
print(p1 ^ p2)

# 17.Numere unice într-o matrice
rows = int(input("Număr de rânduri: "))
mat = [list(map(int, input().split())) for _ in range(rows)]
rez = set(x for r in mat for x in r)
print(rez)

# 18.Verificare anagrame
w1 = input("Cuvânt 1: ").lower()
w2 = input("Cuvânt 2: ").lower()
print(set(w1) == set(w2))

# 19.Unificarea datelor din mai multe surse
A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))
C = set(map(int, input("Set C: ").split()))
print("Comune tuturor:", A & B & C)
print("Apar in cel putin unul:", A | B | C)
print("Unice A:", A - (B | C))
print("Unice B:", B - (A | C))
print("Unice C:", C - (A | B))

# 20.Diferență simetrică avansată
A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))
C = set(map(int, input("Set C: ").split()))
rez = (A ^ B) ^ C
print(rez)
