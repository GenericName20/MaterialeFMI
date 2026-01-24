#1)
# Citirea lui T (prima linie)
T = int(input())

# Citirea textului (a doua linie). Folosim input() simplu
# pentru a simula citirea textului complet.
text_raw = input().lower()

# 1. Tokenizare (separarea cuvintelor)
# Inlocuim toti separatorii cu spatiu si apoi facem split.
separatori = ".,!?:;-"
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

# Filtram pentru a lua doar cuvintele formate din litere
cuvinte = []

for cuvant in text_raw.split():
    if cuvant.isalpha():  # Verificam sa fie doar litere
        cuvinte.append(cuvant)

n = len(cuvinte)

if T == 1:
    # T=1: Numarul de cuvinte si lista lor
    print(n)
    for cuvant in cuvinte:
        print(cuvant)

elif T == 2:
    # T=2: Cuvantul cel mai mic lexicografic
    min_cuvant = "~"  # Caracter care este sigur mai mare decat orice litera

    for cuvant in cuvinte:
        if cuvant < min_cuvant:
            min_cuvant = cuvant

    if n > 0:
        print(min_cuvant)

elif T == 3:
    # T=3: Numarul de cuvinte care contin secventa 'ini'
    count = 0
    for cuvant in cuvinte:
        if "ini" in cuvant:
            count = count + 1
    print(count)

elif T == 4:
    # T=4: Cuvintele oglindite
    for cuvant in cuvinte:
        oglindit = cuvant[::-1]  # Slicing simplu pentru inversare
        print(oglindit)

elif T == 5:
    # T=5: Numarul de cuvinte care se termina cu 'a'
    count = 0
    for cuvant in cuvinte:
        if cuvant.endswith('a'):
            count = count + 1
    print(count)

elif T == 6:
    # T=6: Lungimea minima si maxima
    if n > 0:
        min_lungime = 51  # Limita maxima + 1
        max_lungime = 0

        for cuvant in cuvinte:
            lungime = len(cuvant)
            if lungime < min_lungime:
                min_lungime = lungime
            if lungime > max_lungime:
                max_lungime = lungime

        print(f"{min_lungime} {max_lungime}")




#2)
text_raw = input().lower()
separatori = ".,!?:;-"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

n = len(cuvinte)
gasit = False

# Parcurgem pana la penultimul cuvant
for i in range(n - 1):
    cuvant1 = cuvinte[i]
    cuvant2 = cuvinte[i + 1]

    if len(cuvant1) == len(cuvant2):
        print(f"{cuvant1} {cuvant2}")
        gasit = True
        break  # Oprim la prima pereche

if not gasit:
    print("NU")


#3)
text_raw = input().lower()
separatori = ".,!?:;-"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

n = len(cuvinte)
prefixe_afisate = []

# Iteram prin cuvinte pentru a mentine ordinea de afisare
for i in range(n):
    cuvant_a = cuvinte[i]

    # Verificam daca acest cuvant a fost deja afisat (pentru unicitate)
    if cuvant_a not in prefixe_afisate:

        este_prefix = False

        # Comparam cuvantul_a cu toate celelalte cuvinte (cuvant_b)
        for j in range(n):
            cuvant_b = cuvinte[j]

            # Conditie 1: Lungimile trebuie sa fie diferite
            if len(cuvant_a) < len(cuvant_b):
                # Conditie 2: cuvant_a sa fie la inceputul lui cuvant_b
                if cuvant_b.startswith(cuvant_a):
                    este_prefix = True
                    break  # Am gasit un singur caz, e suficient

        if este_prefix:
            print(cuvant_a)
            prefixe_afisate.append(cuvant_a)  # Marcam ca afisat


#4)
text_raw = input()  # Citim textul (poate contine Majuscule si Cifre)

# Tokenizare (separatorul este doar spatiul, dar split() se descurca)
cuvinte = text_raw.split()
rezultat = []

for cuvant in cuvinte:
    contine_cifra = False

    # Iteram prin caractere pentru a verifica prezenta unei cifre
    for caracter in cuvant:
        # Verificam daca caracterul este o cifra
        if '0' <= caracter <= '9':
            contine_cifra = True
            break  # Am gasit o cifra, trecem la urmatorul cuvant

    # Daca bucla s-a terminat fara sa gaseasca cifre, adaugam cuvantul
    if not contine_cifra:
        rezultat.append(cuvant)

# Afisam cuvintele ramase, separate prin spatiu
print(" ".join(rezultat))


#5)
litera_c = input().strip().lower()  # Citim litera C
text_raw = input().lower()
separatori = ".,!?:;-"

# Tokenizare (ca in problemele anterioare)
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

for cuvant in cuvinte:
    count = 0
    # Numaram frecventa literei C in cuvant
    for caracter in cuvant:
        if caracter == litera_c:
            count = count + 1

    if count == 2:
        print(cuvant)

#6)
text_raw = input().lower()
separatori = ".,!?:;-"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

for cuvant in cuvinte:
    # Verificam daca lungimea este cel putin 1
    if len(cuvant) > 0:
        prima_litera = cuvant[0]
        ultima_litera = cuvant[-1]

        if prima_litera == ultima_litera:
            print(cuvant)

#7)
text_raw = input().lower()
separatori = ".,!?:;-"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

# Iteram prin lista cuvintelor folosind index (i) si cuvantul propriu-zis
for i in range(len(cuvinte)):
    # Poziția i+1, deci pozitiile impare sunt cand i este par (0, 2, 4...)
    if (i + 1) % 2 != 0:
        print(cuvinte[i])

#8)
text_raw = input().lower()
separatori = ".,!?:;-"
vocale = "aeiou"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

for cuvant in cuvinte:
    count_vocale = 0
    for caracter in cuvant:
        if caracter in vocale:
            count_vocale = count_vocale + 1

    # Verificam conditia: cel putin doua vocale
    if count_vocale >= 2:
        print(cuvant)


#9)
text_raw = input().lower()
vocale = "aeiou"
total_vocale = 0

# Iteram prin TOATE caracterele din text
for caracter in text_raw:
    if caracter in vocale:
        total_vocale = total_vocale + 1

print(total_vocale)

#10)
text_raw = input().lower()
separatori = ".,!?:;-"
vocale = "aeiou"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

for cuvant in cuvinte:
    contine_vocala = False

    for caracter in cuvant:
        if caracter in vocale:
            contine_vocala = True
            break

    # Daca NU contine vocala, inseamna ca are numai consoane
    if not contine_vocala:
        print(cuvant)

#11)
text_raw = input().lower()
separatori = ".,!?:;-"

# Tokenizare
for sep in separatori:
    text_raw = text_raw.replace(sep, " ")

cuvinte = []
for cuvant in text_raw.split():
    if cuvant.isalpha():
        cuvinte.append(cuvant)

initiale = []
for cuvant in cuvinte:
    # Luam doar primul caracter
    if len(cuvant) > 0:
        initiale.append(cuvant[0])

# Afisam initialele separate prin spatiu pe un singur rand
print(" ".join(initiale))


#12)
# Citim cuvantul de eliminat pe prima linie
cuvant_eliminat = input().strip().lower()

# Citim textul pe a doua linie
text_raw = input().lower()

separatori = ".,!?:;-"
rezultat = []

# Prelucram textul pentru a putea itera prin cuvinte si separatori
current_word = ""

# Iteram caracter cu caracter
for caracter in text_raw:
    if caracter.isalpha():
        current_word += caracter
    else:
        # Cand intalnim un separator, procesam cuvantul incheiat
        if current_word:
            if current_word != cuvant_eliminat:
                rezultat.append(current_word)
            current_word = ""

        # Adaugam separatorul inapoi in rezultat
        rezultat.append(caracter)

# Procesam ultimul cuvant (daca textul nu se termina cu separator)
if current_word:
    if current_word != cuvant_eliminat:
        rezultat.append(current_word)

# Unim toate elementele inapoi intr-un singur sir
print("".join(rezultat).strip())

#13)
text_raw = input().lower()
codificare = []

# Iteram prin fiecare caracter
for caracter in text_raw:
    # Verificam daca este litera
    if 'a' <= caracter <= 'z':
        # Calculam pozitia in alfabet: 'a' este 1, 'b' este 2, etc.
        # ord(caracter) returneaza codul ASCII al caracterului
        pozitie = ord(caracter) - ord('a') + 1
        codificare.append(str(pozitie))

# Afisam numerele separate prin spatiu
print(" ".join(codificare))
