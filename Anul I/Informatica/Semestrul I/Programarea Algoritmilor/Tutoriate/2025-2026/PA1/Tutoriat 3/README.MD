## 📘 Introducere

În Python, **colecțiile de date** sunt structuri care permit stocarea și gestionarea mai multor valori într-o singură variabilă.  
Ele sunt esențiale în programare, deoarece facilitează organizarea, procesarea și analizarea datelor.

Cele mai importante tipuri de colecții sunt:
- **Liste (`list`)** – colecții ordonate și modificabile.
- **Tupluri (`tuple`)** – colecții ordonate, dar nemodificabile.
- **Seturi (`set`)** – colecții neordonate, fără elemente duplicate.
- **Dicționare (`dict`)** – perechi cheie-valoare.


---

## 1. Liste (Lists)

### 1.1 Ce este o listă?

O **listă** este o colecție **ordonată**, **mutabilă** și **heterogenă** (poate conține elemente de tipuri diferite).

#### Exemple:
```python
# Listă goală
lista_goala = []

# Listă de numere
numere = [10, 20, 30, 40]

# Listă mixtă
student = ["Ion Popescu", 19, 9.75, True]

# Listă de liste (matrice simplă)
matrice = [[1, 2], [3, 4]]
```

### 1.2 Accesarea elementelor

Fiecare element dintr-o listă are un **index** (poziție), care începe de la `0`.  
De asemenea, putem folosi și index negativ pentru a accesa elementele de la sfârșit.

| Element | Index pozitiv | Index negativ |
| :-----: | :-----------: | :-----------: |
| 10      | 0             | -4            |
| 20      | 1             | -3            |
| 30      | 2             | -2            |
| 40      | 3             | -1            |

#### Exemplu în Python:

```python
numere = [10, 20, 30, 40]

# Accesarea primului element
print(numere[0])   # Output: 10

# Accesarea ultimului element folosind index negativ
print(numere[-1])  # Output: 40
```

### 1.3 Felierea (Slicing)

**Felierea** (slicing) permite extragerea unei **sub-liste** dintr-o listă existentă folosind sintaxa:

```python
lista[start:stop:pas]
```


-start → indexul de la care începe sub-lista (inclusiv)

-stop → indexul la care se oprește sub-lista (exclusiv)

-pas → intervalul de sărituri (implicit 1)

```python
litere = ["a", "b", "c", "d", "e", "f"]
```

```python
# Primele trei elemente
print(litere[0:3])   # ['a', 'b', 'c']

# Toate elementele de la indexul 2 până la sfârșit
print(litere[2:])    # ['c', 'd', 'e', 'f']

# Toate elementele din listă (copie a listei)
print(litere[:])     # ['a', 'b', 'c', 'd', 'e', 'f']

# Elementele cu pas de 2
print(litere[::2])   # ['a', 'c', 'e']

# Elemente în ordine inversă
print(litere[::-1])  # ['f', 'e', 'd', 'c', 'b', 'a']
```

📌 Notă:

-Indexul stop nu este inclus în rezultat.

-Poți folosi și valori negative pentru start și stop pentru a număra de la sfârșitul listei


### 1.4 Modificarea listelor

Listele sunt **mutabile**, ceea ce înseamnă că poți adăuga, modifica sau șterge elemente după ce lista a fost creată.  

#### Operații de adăugare, modificare și ștergere:

| Operație | Descriere | Exemplu |
|----------|-----------|---------|
| `.append(x)` | Adaugă elementul `x` la sfârșitul listei | `lista.append(5)` |
| `.insert(i, x)` | Inserează elementul `x` la poziția `i` | `lista.insert(1, "nou")` |
| `.extend([..])` | Adaugă mai multe elemente din altă listă | `lista.extend([1, 2])` |
| Înlocuire | Schimbă valoarea unui element după index | `lista[0] = "schimbat"` |
| `.remove(x)` | Elimină prima apariție a lui `x` | `lista.remove("b")` |
| `.pop(i)` | Elimină și returnează elementul de la indexul `i` (implicit ultimul) | `ultimul = lista.pop()` |
| `del lista[i]` | Șterge elementul de la indexul `i` | `del lista[2]` |
| `del lista[start:stop]` | Șterge o secțiune (slice) | `del lista[1:3]` |

#### Exemplu practic:

```python
materii = ["Algebra", "Analiza", "Fizica"]

# Adăugare
materii.append("Programare")  # ["Algebra", "Analiza", "Fizica", "Programare"]

# Modificare
materii[1] = "Analiza Matematică"  # ["Algebra", "Analiza Matematică", "Fizica", "Programare"]

# Ștergere după valoare
materii.remove("Fizica")  # ["Algebra", "Analiza Matematică", "Programare"]

# Ștergere după index și returnare
materii.pop(0)  # ["Analiza Matematică", "Programare"]

print(materii)  # Ieșire: ['Analiza Matematică', 'Programare']
```

### 1.5 Funcții și metode utile pentru liste

Aceste funcții și metode sunt folosite frecvent pentru a obține informații sau a manipula listele.

| Funcție / Metodă | Descriere | Exemplu |
|-----------------|-----------|---------|
| `len(lista)` | Returnează **numărul de elemente** din listă | `len([1,2,3])` → `3` |
| `in` (operator) | Verifică dacă o valoare există în listă (True / False) | `"a" in ["a","b","c"]` → `True` |
| `.index(x)` | Returnează **indexul primei apariții** a valorii x (eroare dacă nu există) | `["a","b","c"].index("b")` → `1` |
| `.count(x)` | Numără câte apariții ale lui x există în listă | `["a","b","a"].count("a")` → `2` |
| `.sort()` | Sortează lista **pe loc**, modificând lista originală | `numere.sort()` |
| `sorted(lista)` | Returnează o **listă nouă sortată**, lăsând lista originală neschimbată | `sorted([3,1,2])` → `[1,2,3]` |
| `.reverse()` | Inversează ordinea elementelor **pe loc** | `lista.reverse()` |

#### Exemple practice:

```python
litere = ["c", "a", "b", "a"]

# Lungime
print(len(litere))  # 4

# Apartenență
print("a" in litere)  # True
print("d" in litere)  # False

# Index și număr apariții
print(litere.index("b"))  # 2
print(litere.count("a"))  # 2

# Sortare și inversare
numere = [3, 1, 2]
numere.sort()
print(numere)  # [1, 2, 3]

numere2 = sorted([5, 4, 6])
print(numere2)  # [4, 5, 6]

litere.reverse()
print(litere)  # ['a', 'b', 'a', 'c']

```

### 1.6 Operatori pe liste

Listele pot fi manipulate și cu ajutorul operatorilor de concatenare și repetare.

#### Exemple:

```python
a = [1, 2, 3]
b = [4, 5]

# Concatenare
print(a + b)   # [1, 2, 3, 4, 5]

# Repetiție
print(a * 2)   # [1, 2, 3, 1, 2, 3]

# Verificare apartenență
print(2 in a)  # True
print(6 in b)  # False
```

###  1.7.  List Comprehension 

**List comprehension** este o metodă scurtă și elegantă de a crea liste noi, pornind de la o altă listă (sau o secvență), înlocuind buclele `for` tradiționale.

### 🔹 Sintaxă generală

```python
[expresie for element in secvență if condiție]
```

-expresie → valoarea care va fi adăugată în lista nouă

-for element in secvență → iterarea elementelor

-if condiție → (opțional) filtrează elementele


### Exemple de bază

#### 1️⃣ Generarea unei liste de pătrate

```python
numere = [1, 2, 3, 4, 5]
patrate = [x**2 for x in numere]
print(patrate)  # [1, 4, 9, 16, 25]
```


#### 2️⃣ Filtrarea elementelor pare

```python
numere = [1, 2, 3, 4, 5, 6, 7, 8]
pare = [x for x in numere if x % 2 == 0]
print(pare)  # [2, 4, 6, 8]
```

#### 3️⃣ Aplicarea unei funcții asupra elementelor

```python
cuvinte = ["python", "este", "tare"]
majuscule = [cuvant.upper() for cuvant in cuvinte]
print(majuscule)  # ['PYTHON', 'ESTE', 'TARE']
```

#### 4️⃣ Eliminarea spațiilor dintr-o listă de stringuri

```python
nume = ["  Ana  ", "  Mihai", " Ioana "]
curatate = [n.strip() for n in nume]
print(curatate)  # ['Ana', 'Mihai', 'Ioana']
```

#### 5️⃣ Crearea unei liste de tuple (perechi)

```python
numere = [1, 2, 3, 4]
perechi = [(x, x**2) for x in numere]
print(perechi)  # [(1, 1), (2, 4), (3, 9), (4, 16)]
```

#### 6️⃣ List comprehension cu condiție „if-else”

```python
numere = [1, 2, 3, 4, 5]
rezultat = ["par" if x % 2 == 0 else "impar" for x in numere]
print(rezultat)  # ['impar', 'par', 'impar', 'par', 'impar']

```

#### 7️⃣Aplatizarea unei liste de liste (flattening)

```python
matrice = [[1, 2], [3, 4], [5, 6]]
flat = [x for linie in matrice for x in linie]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

## 2. Tupluri (Tuples)

### 2.1 Ce este un tuplu?

Un **tuplu** este o colecție ordonată, dar **nemodificabilă** (imutabilă).  
Se folosește pentru date fixe, precum coordonate, zilele săptămânii etc.

#### Exemple:

```python
# Tuplu de coordonate
coordonate = (10, 20)

# Tuplu mixt
student = ("Maria", 21, 9.8)

# Tuplu cu un singur element (atenție la virgulă)
tuplu_unic = (5,)
```



### ⚙️ Crearea tuplurilor

Tuplurile se definesc cu **paranteze rotunde** `()` sau pur și simplu prin separare cu virgule.

```python
# Declarații de tupluri
gol = ()
pereche = (1, 2)
auto_creat = 1, 2, 3  # fără paranteze
mix = ("Text", 10, 5.3, True)

# Tuplu cu un singur element
unu = (5,)     # necesară virgula!
nu_tuplu = (5) # acesta este doar un int
```

### 2.2 Accesarea elementelor

Elementele unui tuplu sunt accesate prin **index**, la fel ca în liste. Indexul începe de la `0`.  
De asemenea, se pot folosi **indexi negativi** pentru a începe de la sfârșitul tuplului.

#### Exemplu:

```python
zile = ("Luni", "Marti", "Miercuri", "Joi", "Vineri")

# Accesare prin index pozitiv
print(zile[0])   # Luni
print(zile[2])   # Miercuri

# Accesare prin index negativ
print(zile[-1])  # Vineri
print(zile[-3])  # Miercuri

```
### Slicing (feliere)

```python
Se pot extrage sub-tupluri folosind sintaxa tuplu[start:stop:pas]:
print(zile[1:4])   # ('Marti', 'Miercuri', 'Joi')
print(zile[:3])    # ('Luni', 'Marti', 'Miercuri')
print(zile[::2])   # ('Luni', 'Miercuri', 'Vineri')
```

### 2.3 Operații posibile cu tupluri

| Operație      | Exemplu             | Rezultat                   |
|---------------|-------------------|----------------------------|
| Concatenare   | (1, 2) + (3, 4)   | (1, 2, 3, 4)              |
| Repetiție     | (1, 2) * 3        | (1, 2, 1, 2, 1, 2)        |
| Lungime       | len((1,2,3))      | 3                          |
| Apartenență   | 3 in (1,2,3)      | True                       |

### 2.4 Conversii listă ↔ tuplu

```python
# Listă → Tuplu
lista = [1, 2, 3]
tuplu = tuple(lista)
print(tuplu)  # (1, 2, 3)

# Tuplu → Listă
lista2 = list(tuplu)
print(lista2)  # [1, 2, 3]

```
### 2.5 Dezasamblarea (unpacking)

```python
# Exemplu de unpacking
date = ("Andrei", (2003, "Cluj"))
nume, (an, oras) = date

print(f"{nume} s-a născut în {an} la {oras}.")
# Ieșire: Andrei s-a născut în 2003 la Cluj.
```
