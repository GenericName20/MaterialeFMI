#Operatii matematice
import math #pentru a putea face radical
from operator import truediv

n = int(input("n = "));
print (f'\nPatratul: {n*n}\nCubul: {n**3}')
#putem folosi si pow(e,p)
if (n>0):
    print (f'Radacina patrata: {round(math.sqrt(n),2)}')
    print (f'Radacina patrata: {round(pow(n,1/2),2)}')
    # pentru a afisa cu un nr anumit de zecimale nr = round(x,nr_zecimale)

#Cautare subsir
sir = input("Introduceti sirul: ")
subsir = input("Introduceti subsirul: ")

cnt = 0
print("Pozitii:", end=" ")

while True:
    poz = sir.find(subsir, cnt)
    if poz == -1:
        break
    print(poz, end=" ")
    cnt = poz + len(subsir)  # Evităm suprapunerea

print()  # Linie nouă la final


##Suma cifrelor si invers
n = input("Introdu numarul: ")
print("Palindrom:", end=" ")
if (n == n[::-1]):
    print("DA", end = "\n")
else:
    print("NU", end="\n")
print("Ultima cifra", end=" ")
if(int(n[-1])%2==0):
    print("para")
else:
    print("impara")


##Inlocuire caractere
s = input("Introduceti sirul: ")
vechi = input("Introduceti sirul pe care vreti sa-l inlocuiti: ")
nou = input("Introduceti sirul cu care vreti sa inlocuiti")
s = s.replace(vechi,nou)
print(s)



##Numar prim si suma divizorilor
n = int(input("Introduceti numarul: "))
s = 0
cnt = 0
for i in range(1,math.trunc(math.sqrt(n))+1):
    if (n%i==0):
        cnt+=1
        s+=i
        if i != n//i :
            s+=n//i #asa evitam sa l punem de 2 ori daca e patrat perfect

if  cnt == 1 :
    print("da")
else:
    print("nu")

print(f"Suma este {s}")


##Numar aparitii subsir
sir = input("Introdu sirul :")
subsir = (input("Introdu subdirul :"))
print(f'Numarul de aparitii {sir.count(subsir)}')\



##Cifrul lui Cezar
text = input("Introdu textul: ").upper()
k = int(input("Introdu mumarul: "))

for i in range(len(text)):
    if ord(text[i])+k>90:
        poz = 65+(ord(text[i])+k-90)-1
    else:
        poz = ord(text[i]) + k
    if text[i]==" ":
        print(" ")
    else:
        print(chr(poz), end="")

##Fibonacci si diferente
n = int(input("Introdu numarul: "))

f1 = 0
f2 = 1
fibo = ""

if n == 0:
    fibo += str(f1)
elif n == 1:
    fibo += str(f1) + " " + str(f2)
else:
    fibo += str(f1) + " " + str(f2)
    cnt = 2
    while cnt < n:
        f3 = f1 + f2
        fibo += " " + str(f3)
        f1 = f2
        f2 = f3
        cnt += 1

print("Sirul Fibonacci:", fibo)
diferente = fibo.split()
for i in range(len(diferente)-1):
    print(int(diferente[i+1])-int(diferente[i]), end= " ")


##Piramida numerica
n = int(input("Introdu numarul: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end= " ")
    print("\n")

for i in range(n,0,-1):
    for j in range(1,i):
        print(j, end= " ")
    print("\n")



##Conversii si proprietati numerice
n = float(input("Introduceti numarul :"))
print (f"Patrat {n*n}")
print (f"Cub {pow(n,3)}")
if (n!=0):
    print (f"Invers {pow(n,-1)}")
print (f"Modul {abs(n)}")
print(f"Rotunjire: {n:.2f}")