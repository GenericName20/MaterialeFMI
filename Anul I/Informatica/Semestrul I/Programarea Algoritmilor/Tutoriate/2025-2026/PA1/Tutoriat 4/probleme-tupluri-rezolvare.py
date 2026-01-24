# Probleme tupluri

# 1.Sortare după al doilea element Ai o listă de tupluri (nume, notă). Sorteaz-o după notă, crescător.
elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
rez = sorted(elevi, key=lambda x: x[1])
print(rez)

# 2.Sortare descrescătoare după al doilea element Aceeași listă, dar sortată descrescător după notă.
rez = sorted(elevi, key=lambda x: x[1], reverse=True)
print(rez)

# 3.Filtrare după condiție numerică Afișează doar elevii cu nota peste 8.
elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
rez = [e for e in elevi if e[1] > 8]
print(rez)

# 4.Căutare într-o listă de tupluri Verifică dacă un elev există în listă după nume.
elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
nume = "Ion"
exista = any(e[0] == nume for e in elevi)
print(exista)

# 5.Calcularea mediei notelor Calculează media notelor dintr-o listă de tupluri (nume, notă).
elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
media = sum(e[1] for e in elevi) / len(elevi)
print(media)

# 6.Afișarea elevului cu cea mai mare notă Folosește max() cu un key pentru a găsi elevul cu nota maximă.
elevi = [("Ana", 10), ("Ion", 8), ("Maria", 9)]
top = max(elevi, key=lambda x: x[1])
print(top)

# 7.Afișarea elevului cu cea mai mică notă Similar, dar cu min().
low = min(elevi, key=lambda x: x[1])
print(low)

# 8.Eliminarea tuplurilor duplicate Elimină tuplurile identice dintr-o listă.
note = [("Ana", 10), ("Ion", 8), ("Ana", 10)]
rez = list(set(note))
print(rez)

# 9.Sortare după lungimea numelui Sortează elevii după lungimea numelui.
rez = sorted(elevi, key=lambda x: len(x[0]))
print(rez)

# 10.Inversarea perechilor (nume, notă) Creează o nouă listă cu tupluri inversate (notă, nume).
inversate = [(n, m) for m, n in elevi]
print(inversate)

# 11.Calculul sumei notelor pare Suma notelor care sunt pare.
suma_pare = sum(n for _, n in elevi if n % 2 == 0)
print(suma_pare)

# 12.Sortare după ultima cifră a notei Sortează tuplurile după ultima cifră a notei.
rez = sorted(elevi, key=lambda x: x[1] % 10)
print(rez)

# 13.Filtrare pe bază de inițială Afișează doar elevii al căror nume începe cu „A”.
rez = [e for e in elevi if e[0].startswith("A")]
print(rez)

# 14.Concatenarea a două liste de tupluri Combină două liste de tupluri într-una singură.
a = [("Ana", 10)]
b = [("Ion", 9), ("Maria", 8)]
rez = a + b
print(rez)

# 15.Calcularea diferenței între note maxime și minime Determină diferența între nota maximă și minimă.
max_nota = max(e[1] for e in elevi)
min_nota = min(e[1] for e in elevi)
print(max_nota - min_nota)

# 16.Sortare dublă (după notă, apoi nume) Sortează mai întâi după notă, apoi alfabetic.
rez = sorted(elevi, key=lambda x: (x[1], x[0]))
print(rez)

# 17.Crearea de tupluri din fișier text Fișierul note.txt conține: Ana 10 Ion 8 Maria 9 Citește fișierul și creează o listă de tupluri.
with open("note.txt") as f: elevi = [(l.split()[0], int(l.split()[1])) for l in f]
print(elevi)

# 18.Transformarea unei liste de șiruri în tupluri Listează și transformă datele în tupluri (nume, nota).
linii = ["Ana 10", "Ion 8", "Maria 9"]
rez = [tuple([p[0], int(p[1])]) for p in (line.split() for line in linii)]
print(rez)

# 19.Suma notelor tuturor elevilor din tupluri Adună toate notele dintr-un tuplu de tupluri.
note = ((10, 9), (8, 7), (9, 10))
suma = sum(sum(t) for t in note)
print(suma)

# 20.Sortare după media notelor din tuplu Fie o listă de tupluri (nume, (nota1, nota2)). Calculează media și sortează crescător.
elevi = [("Ana", (10, 9)), ("Ion", (8, 7)), ("Maria", (9, 10))]
rez = sorted(elevi, key=lambda x: sum(x[1]) / len(x[1]))
print(rez)