## 1. Tupluri (Tuples)

### 1.1 Ce este un tuplu?

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



###  Crearea tuplurilor

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

### 1.2 Accesarea elementelor

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

### 1.3 Operații posibile cu tupluri

| Operație      | Exemplu             | Rezultat                   |
|---------------|-------------------|----------------------------|
| Concatenare   | (1, 2) + (3, 4)   | (1, 2, 3, 4)              |
| Repetiție     | (1, 2) * 3        | (1, 2, 1, 2, 1, 2)        |
| Lungime       | len((1,2,3))      | 3                          |
| Apartenență   | 3 in (1,2,3)      | True                       |

### 1.4 Conversii listă ↔ tuplu

```python
# Listă → Tuplu
lista = [1, 2, 3]
tuplu = tuple(lista)
print(tuplu)  # (1, 2, 3)

# Tuplu → Listă
lista2 = list(tuplu)
print(lista2)  # [1, 2, 3]

```
### 1.5 Dezasamblarea (unpacking)

```python
# Exemplu de unpacking
date = ("Andrei", (2003, "Cluj"))
nume, (an, oras) = date

print(f"{nume} s-a născut în {an} la {oras}.")
# Ieșire: Andrei s-a născut în 2003 la Cluj.
```


## 2. Seturi (Sets)

### 2.1 Ce este un set?

Un **set** este o colecție neordonată de elemente **unice**.  
Asta înseamnă:

- nu reține ordinea elementelor  
- nu permite duplicate  

Seturile sunt utile pentru a elimina valori duplicate, pentru verificări rapide de apartenență și pentru operații de tip mulțimi (uniune, intersecție etc.).

#### Exemple:

```python
# Un set simplu
fructe = {"mar", "banana", "cirese"}

# Set cu tipuri diferite
mix = {1, "text", True, 3.14}

# Set gol (mare atenție!)
gol = set()      # corect
nu_set = {}      # dicționar gol
```

### 2.2 Crearea seturilor

Seturile se definesc cu accolade {} sau prin funcția set().

```python
# Declarații de seturi
s1 = {1, 2, 3}
s2 = set([4, 5, 6])
s3 = set("banana")   # elimina duplicatele → {'b', 'a', 'n'}

# Duplicate ignorate
s4 = {1, 2, 2, 3, 3}
print(s4)  # {1, 2, 3}
```

### 2.3 Operații pe seturi

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

| Operație | Exemplu | Rezultat |
|----------|---------|----------|
| Uniune | `A \| B` | `{1, 2, 3, 4, 5, 6}` |
| Intersecție | `A & B` | `{3, 4}` |
| Diferență | `A - B` | `{1, 2}` |
| Diferență simetrică | `A ^ B` | `{1, 2, 5, 6}` |

### 2.4 Adăugare și ștergere de elemente

```python
s = {1, 2, 3}

# Adăugare
s.add(4)

# Adăugare multiplă
s.update([5, 6], {7, 8})

# Ștergere
s.remove(3)     # eroare dacă nu există
s.discard(100)  # nu dă eroare

# Elimină și întoarce un element aleator
s.pop()
```

### 2.5 Metode și functii

| Metodă / Funcție | Exemplu | Descriere |
|------------------|---------|-----------|
| `add(elem)` | `s.add(5)` | Adaugă un element în set. |
| `update(iterabile)` | `s.update([1,2], {3,4})` | Adaugă mai multe elemente dintr-un iterabil. |
| `remove(elem)` | `s.remove(3)` | Șterge un element; dă eroare dacă nu există. |
| `discard(elem)` | `s.discard(3)` | Șterge un element; nu dă eroare dacă nu există. |
| `pop()` | `s.pop()` | Elimină și returnează un element aleatoriu. |
| `clear()` | `s.clear()` | Golește complet setul. |
| `len(set)` | `len(s)` | Returnează numărul de elemente. |
| `elem in set` | `3 in s` | Verifică apartenența unui element. |
| `set.copy()` | `s.copy()` | Creează o copie superficială a setului. |

### 2.6 Conversii listă ↔ set
```python
# Listă → Set (elimină duplicatele)
lista = [1, 2, 2, 3, 3, 3]
s = set(lista)
print(s)  # {1, 2, 3}

# Set → Listă
lista2 = list(s)
print(lista2)  # [1, 2, 3] (ordinea nu este garantată)
```





