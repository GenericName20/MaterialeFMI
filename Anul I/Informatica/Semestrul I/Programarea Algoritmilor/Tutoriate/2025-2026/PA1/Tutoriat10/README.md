# Rezolvare subiecte colocviu și examen

-----


## SUBIECT EXAMEN(2025)

### Cerințele examenului:
1.  **Subiectul I** este obligatoriu.
2.  Dintre subiectele II, III și IV trebuie alese **CEL MULT DOUĂ**.

### 1. Subiectul I - `subiect_1.py`
Acest fișier conține rezolvarea celor trei subpuncte obligatorii:
* **a) Funcția `consoane_comune`**: Primește un număr variabil de cuvinte și returnează numărul maxim de cuvinte care au exact aceeași mulțime de consoane.
* **b) List Comprehension (`prefix_5`)**: Filtrarea unei liste de numere astfel încât să rămână doar cele care nu sunt multipli de 5 și nu au prefixe multipli de 5.
* **c) Analiza complexității**: Determinarea complexității (în cel mai defavorabil caz) pentru o funcție recursivă dată `f(s)`, care împarte șirul în jumătăți (Divide et Impera).
  Se consideră funcția recursivă `f(s)`, unde `n = len(s)`.

## Analiza complexității (Teorema Master)

### Observații

- La fiecare apel recursiv se face **un singur apel** pe aproximativ **jumătate din șir**:
  - `f(s[m+1:])` sau `f(s[:m+1])` → dimensiune ≈ `n / 2`

- În fiecare apel există operații cu **cost liniar `O(n)`**:
  - `replace(...)` – parcurge întregul șir
  - slicing (`s[:...]`, `s[...]`) – copiere de subșiruri
  - concatenare de șiruri

---

### Recurența

\[
T(n) = T(n/2) + O(n)
\]

---

### Aplicarea Teoremei Master

- $a = 1$
- $b = 2$
- $f(n) = \Theta(n)$

Calculăm:

$$
n^{\log_b a} = n^{\log_2 1} = n^0 = 1
$$

Deoarece:

$$
f(n) = \Theta(n) \gg 1
$$

rezultă că ne aflăm în **cazul 3 al Teoremei Master**.

### Concluzie

\[
T(n) = \Theta(n)
\]

**Complexitatea temporală (worst-case) este liniară.**


### 2. Subiectul II (Metoda Greedy) - `subiect_2.py`
**Problema:** Alimentarea mașinilor cu canistre de benzină.
* **Descriere:** Se dau $n$ mașini cu necesar de benzină și $m$ canistre cu capacități date. O mașină poate primi o singură canistră.
* **Obiectiv:** Maximizarea numărului de mașini care ajung la destinație.
* **Complexitate:** $O(N \log N)$ (bazată pe sortarea mașinilor și a canistrelor).
* **Output:** Numărul de mașini și perechile `Mașină -> Canistră`.

### 3. Subiectul III (Programare Dinamică) - `subiect_3.py`
**Problema:** Tăierea barei de metal (Rod Cutting Problem variation).
* **Descriere:** Un meșteșugar are o bară de lungime $L$ și comenzi pentru bucăți de lungimi $l_i$ cu prețuri $p_i$.
* **Obiectiv:** Maximizarea câștigului total prin tăierea barei.
* **Complexitate:** $O(k \cdot L)$, unde $k$ este numărul de tipuri de bucăți și $L$ lungimea barei.
* **Output:** Câștigul maxim și lungimile bucăților tăiate (afișate crescător).

### 4. Subiectul IV (Backtracking) - `subiect_4.py`
**Problema:** Generare coduri PIN "mega-sigure".
* **Descriere:** Generarea codurilor de lungime $n$ care:
    * Nu au cifre nule.
    * Nu au cifre alăturate egale.
    * Orice cifră apare de cel mult $p$ ori.
* **Output:** Toate codurile care respectă condițiile și numărul total al acestora.


------ 

## SUBIECT COLCVIU 1

---

### 1. Subiectul I – Lucrul cu matrice și mulțimi – `colocviu_1.py`

#### a) Funcția `citire_matrice`
- **Descriere:** Primește ca parametru numele unui fișier care conține elementele unei matrice.
- **Comportament:**
  - Citește matricea din fișier (elemente separate prin spațiu).
  - Dacă numărul de elemente diferă de la o linie la alta, funcția returnează `None`.
- **Returnează:** matricea citită sau `None`.

#### b) Funcția `multimi`
- **Parametri:**
  - o matrice
  - un număr variabil de indici ai liniilor
- **Pentru fiecare linie selectată:**
  - se construiește mulțimea numerelor **negative**
  - se construiește mulțimea numerelor **pozitive** care au **prima cifră egală cu ultima**
- **Returnează:**
  - intersecția mulțimilor numerelor negative
  - reuniunea mulțimilor numerelor pozitive (elemente distincte)

#### c) Prelucrare fișier `matrice.in`
- Se citește matricea folosind `citire_matrice`.
- Se folosesc apeluri utile ale funcției `multimi`.
- Se afișează:
  - numerele pozitive cu prima cifră egală cu ultima de pe **ultimele 3 linii**, ordonate crescător
  - numărul de elemente negative comune **primei și ultimei linii**

---

### 2. Subiectul II – Șiruri de caractere și liste – `colocviu_2.py`

#### a) Funcția `modifica_prefix`
- **Parametri:** `x`, `y`, `prop`
- **Descriere:**
  - În fiecare cuvânt din propoziție care începe cu `x`, prefixul `x` este înlocuit cu `y`.
- **Returnează:**
  - propoziția modificată
  - numărul de cuvinte modificate

#### b) Funcția `poz_max`
- **Parametru:** listă de numere naturale
- **Returnează:** lista pozițiilor (numerotate de la 1) unde apare valoarea maximă.

#### c) Prelucrare fișier `propozitii.in`
- Se citesc două cuvinte `a` și `b` de la tastatură.
- Se creează fișierul `propozitii_modificate.out` folosind `modifica_prefix`.
- Se determină propozițiile cu cele mai multe modificări.
- Se afișează indicii acestora folosind funcția `poz_max`.

---

### 3. Subiectul III – Structuri de date (autori și cărți) – `colocviu_3.py`

#### a) Memorarea datelor
- Datele din fișierul `autori.in` sunt memorate într-o **singură structură de date** (dicționar).
- Structura permite:
  - acces rapid la autor după cod
  - acces rapid la cărți după codul autorului

#### b) Funcția `sterge_carte`
- **Parametri:**
  - structura de date
  - codul unei cărți
- **Comportament:**
  - șterge cartea dacă există
  - returnează numele autorului sau `None`
- **Afișare:**
  - mesaj corespunzător existenței cărții
  - structura rămasă după ștergere

#### c) Funcția `carti_autor`
- **Parametri:**
  - structura de date
  - codul unui autor
- **Returnează:**
  - numele autorului
  - lista cărților sale, sub forma:
    `(titlu, an_aparitie, nr_pagini)`
- **Sortare:**
  - crescător după an
  - descrescător după numărul de pagini
  - crescător după titlu

Dacă autorul nu există, funcția returnează o listă vidă.

---



## SUBIECT COLOCVIU 2 (2025)


---

## Subiectul 1 – Fișiere și matrice 

### a) Citirea matricei din fișier
- Se citește fișierul `matrice.in`.
- Fiecare linie conține elementele unei linii din matrice, separate prin spațiu.
- Dacă liniile nu au același număr de elemente, funcția returnează `None`.

**Idee simplă:**
- citim linie cu linie
- transformăm fiecare linie în listă de numere
- verificăm dacă toate liniile au aceeași lungime

---

### b) Funcția `multimi`
- Primește:
  - o matrice
  - indici de linii (număr variabil de parametri)
- Pentru fiecare linie:
  - construim mulțimea numerelor **negative**
  - construim mulțimea numerelor **pozitive** cu prima cifră egală cu ultima
- Returnăm:
  - **intersecția** numerelor negative
  - **reuniunea** numerelor pozitive (distincte)

---

### c) Prelucrarea fișierului
- Se folosesc funcțiile de la a) și b)
- Se afișează:
  - numerele pozitive cu prima cifră egală cu ultima din **ultimele 3 linii**, ordonate crescător
  - numărul de elemente negative comune **primei și ultimei linii**

---

## Subiectul 2 – Șiruri de caractere 

### a) Funcția `modifica_prefix(x, y, prop)`
- Pentru fiecare cuvânt din propoziție:
  - dacă începe cu `x`, prefixul `x` este înlocuit cu `y`
- Returnează:
  - propoziția modificată
  - numărul de cuvinte modificate

**Idee simplă:**
- împărțim propoziția în cuvinte (`split`)
- verificăm `startswith(x)`
- reconstruim propoziția

---

### b) Funcția `poz_max`
- Primește o listă de numere
- Returnează pozițiile (numerotate de la 1) unde apare valoarea maximă

---

### c) Fișierele `propozitii.in` → `propozitii_modificate.out`
- Se citesc cuvintele `a` și `b`
- Se modifică propozițiile folosind `modifica_prefix`
- Se determină propozițiile cu cele mai multe modificări
- Se afișează indicii acestora folosind `poz_max`

---

## Subiectul 3 – Structuri de date (bănci și depozite) 

### a) Memorarea datelor
- Datele din `depozite.in` sunt memorate într-o **singură structură de date**
- Structura permite:
  - acces rapid la depozite după bancă
  - grupare după monedă

**Structură simplă (exemplu):**
```text
{
  "Banca Transilvania": {
      "LEI": [ (suma, dobanda, perioada), ... ],
      "EURO": [ ... ]
  },
  ...
}
```


