# Dicționare în Python

Un dicționar (dict) este o colecție mutabilă de perechi cheie: valoare

 1.Este o structură de date asociativă (sau tablou asociativ)

 2.Accesarea elementelor se realizează prin cheia lor, nu prin poziția (indexul) lor

 3.Cheile trebuie să fie unice și imutabile (hashable)

 4.Valorile nu au nicio restricție

 5.Păstrează ordinea de inserare a cheilor 

 6.Operațiile de inserare, accesare și ștergere au o complexitate medie constantă de O(1).

## 1.Proprietați

| Proprietate            | Descriere                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------|
| **1. Asociative**      | Stochează date ca perechi **cheie: valoare**                                                             |
| **2. Mutabile**        | Conținutul dicționarului poate fi modificat după creare (adăugare, ștergere, actualizare)               |
| **3. Indexate prin cheie** | Accesarea elementelor se face prin **cheia** asociată, nu printr-un index numeric                     |
| **4. Ordinea păstrată** | Începând cu Python 3.7, dicționarele păstrează **ordinea de inserare** a cheilor                        |

## 2.Cerințe pentru Chei
Cheile unui dicționar trebuie să îndeplinească două condiții stricte:

-Unice: Fiecare cheie dintr-un dicționar trebuie să fie unică.


-Imutabile (Hashable): Cheile trebuie să fie de un tip de date imutabil (e.g., str, int, float, tuple format din elemente imutabile).

## 3.Crearea și Manipularea

### 3.1. Inițializare Standard

Se folosesc acolade ({}) și perechi cheie: valoare separate prin virgulă.

```python
# Dicționar vid
d_vid = {}
print(f"Dicționar vid: {d_vid}")
# Ieșire: {}

# Dicționar cu date
student = {
    "ID": 101,
    "Nume": "Popescu Andrei",
    "Nota": 9.50,
    (1, 2, 3): "Tuplu ca cheie" # Cheile pot fi neomogene [cite: 381]
}
print(f"Dicționar student: {student}")
# Ieșire: {'ID': 101, 'Nume': 'Popescu Andrei', 'Nota': 9.5, (1, 2, 3): 'Tuplu ca cheie'}
```

### 3.2. Accesarea, Inserarea și Ștergerea

Accesarea sau inserarea/modificarea se face prin specificarea cheii între paranteze drepte d[cheie].

```python
d = {"marca": "Toyota", "model": "Corolla", "an": 2020}

# Accesare
an_fabricatie = d["an"]
print(f"Anul de fabricație: {an_fabricatie}") # Ieșire: 2020

# Modificare valoare asociată unei chei existente
d["an"] = 2022
print(f"Dicționar după modificare: {d}") # Ieșire: {'marca': 'Toyota', 'model': 'Corolla', 'an': 2022}

# Inserare pereche cheie: valoare nouă
d["culoare"] = "roșu"
print(f"Dicționar după inserare: {d}") # Ieșire: {'marca': 'Toyota', 'model': 'Corolla', 'an': 2022, 'culoare': 'roșu'}

# Ștergerea unei chei
del d["an"]
print(f"Dicționar după ștergere: {d}") # Ieșire: {'marca': 'Toyota', 'model': 'Corolla', 'culoare': 'roșu'}
```

### 3.3. Evitarea Erorii KeyError

Încercarea de a accesa o cheie inexistentă va lansa o eroare de tipul KeyError. Pentru a evita acest lucru, se pot folosi două metode:

### A.Testarea Existenței Cheii

Se folosește operatorul in pentru a verifica dacă o cheie există în dicționar.

```python
d = {'A': 10, 'B': 20}
cheie_cautata = 'C'

if cheie_cautata in d: # operatorul in testează existența cheii [cite: 553]
    print(f"d['{cheie_cautata}'] = {d[cheie_cautata]}")
else:
    print(f"Cheia '{cheie_cautata}' nu apare în dicționar!")
# Ieșire: Cheia 'C' nu apare în dicționar!
```

### B. Utilizarea Metodei get()

Metoda get(cheie, [valoare_eroare]) returnează valoarea asociată cheii sau None (sau o valoare implicită setată) dacă cheia nu există, fără a genera eroare.

```python
d = {'A': 10, 'B': 20}

# get() fără valoare implicită (returnează None dacă lipsește)
valoare_A = d.get('A')
valoare_Z = d.get('Z')
print(f"Valoare pentru 'A': {valoare_A}") # Ieșire: 10
print(f"Valoare pentru 'Z': {valoare_Z}") # Ieșire: None

# get() cu valoare implicită
valoare_default = d.get('X', -1) # -1 este valoarea implicită [cite: 606]
print(f"Valoare pentru 'X': {valoare_default}") # Ieșire: -1
```

## 4.Metode pentru Vizualizări (Views)

Dicționarele oferă metode pentru a obține vizualizări dinamice (views) ale cheilor, valorilor sau perechilor. Aceste vizualizări sunt iterabile și se actualizează automat la modificarea dicționarului.

| Metodă     | Returnează     | Descriere                                           |
|------------|----------------|------------------------------------------------------|
| `keys()`   | `dict_keys`    | O vizualizare a tuturor cheilor                     |
| `values()` | `dict_values`  | O vizualizare a tuturor valorilor                   |
| `items()`  | `dict_items`   | O vizualizare a tuturor perechilor (cheie, valoare) |

```python
d = {'E': 20, 'D': 7, 'A': 10}

chei = d.keys()
valori = d.values()
perechi = d.items()

print(f"Chei: {list(chei)}") # Vizualizările pot fi convertite în liste [cite: 632]
print(f"Valori: {list(valori)}")
print(f"Perechi: {list(perechi)}")

# Modificarea dicționarului modifică vizualizarea (View-ul este dinamic)
d['K'] = 1000
print(f"\nChei noi (după d['K'] = 1000): {list(chei)}")
# Ieșire: ['E', 'D', 'A', 'K']
```

## 5.Operații de Actualizare și Ștergere

### *Metoda update()*
Metoda update(dicționar) actualizează dicționarul curent cu perechile dintr-un alt dicționar (sau secvență de perechi). Dacă o cheie există, valoarea ei se actualizează; altfel, se adaugă o cheie nouă.

```python
d1 = {'A': 10, 'B': 20}
d2 = {'B': -5, 'C': 30} # 'B' se actualizează, 'C' se adaugă

d1.update(d2)
print(f"Dicționarul d1 după update: {d1}")
# Ieșire: {'A': 10, 'B': -5, 'C': 30}
```

### *Metoda pop()*
Metoda pop(cheie, [valoare_implicită]) șterge cheia specificată din dicționar și returnează valoarea ei asociată.

Dacă cheia nu există și nu este setată o valoare implicită, se lansează KeyError.

```python
d = {'X': 100, 'Y': 200, 'Z': 300}

# Pop normal
val_X = d.pop('X')
print(f"Valoare eliminată ('X'): {val_X}") # Ieșire: 100

# Pop cu valoare implicită (cheia 'W' nu există, returnează None)
val_W = d.pop('W', None)
print(f"Valoare eliminată ('W'): {val_W}") # Ieșire: None

print(f"Dicționar final: {d}") # Ieșire: {'Y': 200, 'Z': 300}
```

### *Metoda clear()*
Metoda clear() șterge toate elementele (perechile cheie: valoare) din dicționar, lăsându-l vid

### 6.Complexitatea Computațională

Dicționarele sunt structuri de date de bază pentru algoritmi performanți, datorită complexității reduse a operațiilor cheie.

| Operație / Metodă / Funcție                 | Complexitate Medie | Complexitate Maximă |
|---------------------------------------------|---------------------|----------------------|
| Testare apartenență (cheie) (`in`, `not in`) | $\mathcal{O}(1)$    | $\mathcal{O}(n)$     |
| Accesare element prin cheie                 | $\mathcal{O}(1)$    | $\mathcal{O}(n)$     |
| Ștergere element (`del`, `pop`)             | $\mathcal{O}(1)$    | $\mathcal{O}(n)$     |
| Creare                                     | $\mathcal{O}(n)$    | $\mathcal{O}(n^2)$   |





-------------------------------------------
## Exemplu: Sistem de Catalog de Produse

Vom folosi un dicționar numit catalog_produse unde:

 1.Cheia Externă: Reprezintă Categoria de Produs (ex: "Electronice").

 2.Valoarea Externă (Dicționar Intern): Reprezintă o colecție de produse din acea categorie.

 3.Cheia Internă: Este Codul Unic al Produsului (ex: "LPT101").

 4.Valoarea Internă (Dicționarul Cel Mai Intern): Conține detaliile produsului (nume, preț, stoc).


```python
catalog_produse = {
    "Electronice": {
        "LPT101": {"nume": "Laptop Ultra", "pret": 4500.00, "stoc": 12},
        "TLF202": {"nume": "Telefon X", "pret": 2800.00, "stoc": 55},
        "CST303": {"nume": "Casti Bluetooth", "pret": 450.00, "stoc": 80}
    },
    "Carti": {
        "RMB11A": {"nume": "Roman Modern", "pret": 55.00, "stoc": 200},
        "PRS22B": {"nume": "Proza Scurta", "pret": 32.50, "stoc": 150}
    }
}
```

1. Accesarea Detaliilor unui Produs Specific
```python
#Pentru a accesa prețul unui produs specific, navigăm prin două chei: [Categorie][Cod Produs].

cod_produs = "TLF202"
categorie = "Electronice"

# Accesare directă: O(1) + O(1) = Timp constant mediu
pret_telefon = catalog_produse[categorie][cod_produs]["pret"]
print(f"Prețul telefonului {cod_produs} este: {pret_telefon} RON")
# Ieșire: Prețul telefonului TLF202 este: 2800.0 RON
```

2.Actualizarea Stocului
```python
#Actualizarea stocului se face la fel de rapid.
cod_produs = "LPT101"
categorie = "Electronice"

# Actualizăm stocul laptopului

catalog_produse[categorie][cod_produs]["stoc"] -= 5
stoc_nou = catalog_produse[categorie][cod_produs]["stoc"]
print(f"Stoc nou pentru Laptop Ultra: {stoc_nou} bucăți.")
# Ieșire: Stoc nou pentru Laptop Ultra: 7 bucăți.
```

3. Inserarea unui Produs Nou într-o Categorie Existentă
```python
produs_nou = {
    "DRN404": {"nume": "Dronă Foto", "pret": 1800.00, "stoc": 30}
}
categorie = "Electronice"

# Folosim metoda update() pentru a adăuga noul produs în dicționarul intern
catalog_produse[categorie].update(produs_nou)

print(f"Produsul Drona Foto a fost adăugat în {categorie}.")
print(catalog_produse[categorie]["DRN404"])
# Ieșire: {'nume': 'Dronă Foto', 'pret': 1800.0, 'stoc': 30}
```

4.Adăugarea unei Categorii Noi
```python
categorie_noua = "Jucarii"
produs_jucarie = {
    "PPA10": {"nume": "Păpușă Articulată", "pret": 75.00, "stoc": 100}
}

# Inserarea unei noi perechi (cheie: dicționar) în catalogul principal
catalog_produse[categorie_noua] = produs_jucarie

print(f"Noua categorie adăugată: {categorie_noua}")
print(catalog_produse["Jucarii"])
# Ieșire: {'PPA10': {'nume': 'Păpușă Articulată', 'pret': 75.0, 'stoc': 100}}
```
