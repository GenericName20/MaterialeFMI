#Seturi în Python
---

### 1️⃣ Eliminarea dublurilor
Scrie un program care primește o listă de numere și afișează lista fără elemente duplicate, folosind un `set`.

**Input:**
```python
[1, 2, 2, 3, 4, 4, 5]
```

**Output:**
```python
{1, 2, 3, 4, 5}
```

---

### 2️⃣ Verificarea apartenenței
Primește un număr de la tastatură și verifică dacă acesta se află într-un set prestabilit de valori.

**Input:**
```python
numere = {2, 4, 6, 8, 10}
x = 6
```

**Output:**
```python
6 se află în set.
```

---

### 3️⃣ Operații de bază
Creează două seturi `A` și `B` și afișează reuniunea, intersecția și diferența.

**Input:**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

**Output:**
```python
Reuniune: {1, 2, 3, 4, 5, 6}
Intersecție: {3, 4}
Diferență A - B: {1, 2}
```

---

### 4️⃣ Cardinalul unui set
Primește o listă de cuvinte și afișează câte cuvinte unice conține.

**Input:**
```python
cuvinte = ["mere", "pere", "mere", "prune"]
```

**Output:**
```python
Sunt 3 cuvinte unice.
```

---

### 5️⃣ Conversie din șir în set de caractere
Primește un șir și afișează setul de caractere distincte din acel șir.

**Input:**
```python
text = "banana"
```

**Output:**
```python
{'b', 'a', 'n'}
```

---

### 6️⃣ Cuvinte comune între două propoziții
Primește două propoziții și afișează cuvintele comune.

**Input:**
```python
p1 = "pisica doarme pe canapea"
p2 = "cainele doarme in curte"
```

**Output:**
```python
Cuvinte comune: {'doarme'}
```

---

### 7️⃣ Cuvinte distincte totale
Afișează câte cuvinte distincte există în total în două propoziții.

**Input:**
```python
p1 = "soarele rasare dimineata"
p2 = "soarele apune seara"
```

**Output:**
```python
Cuvinte distincte: {'soarele', 'rasare', 'dimineata', 'apune', 'seara'}
Total: 5
```

---

### 8️⃣ Diferență simetrică
Afișează elementele care apar doar într-unul dintre cele două seturi.

**Input:**
```python
A = {1, 2, 3}
B = {3, 4, 5}
```

**Output:**
```python
Diferență simetrică: {1, 2, 4, 5}
```

---

### 9️⃣ Filtrarea elementelor
Elimină toate numerele pare, păstrând doar cele impare.

**Input:**
```python
numere = [1, 2, 3, 4, 5, 6, 7]
```

**Output:**
```python
Set cu numere impare: {1, 3, 5, 7}
```

---

### 🔟 Verificare subset / superset
Verifică relațiile dintre două seturi.

**Input:**
```python
A = {1, 2}
B = {1, 2, 3, 4}
```

**Output:**
```python
A este subset al lui B: True
B este superset al lui A: True
```

---


### 1️⃣1️⃣ Cuvinte unice într-un fișier text
Numără câte cuvinte unice există într-un fișier text.

**Input (conținut fișier):**
```
Ana are mere si merele sunt rosii
```

**Output:**
```python
Cuvinte unice: {'ana', 'are', 'mere', 'si', 'merele', 'sunt', 'rosii'}
Total: 7
```

---

### 1️⃣2️⃣ Intersecția dintre trei seturi
Afișează elementele comune celor trei liste.

**Input:**
```python
A = {1, 2, 3, 4}
B = {2, 3, 5}
C = {0, 2, 3, 9}
```

**Output:**
```python
Intersecție: {2, 3}
```

---

### 1️⃣3️⃣ Caractere comune între cuvinte
Afișează literele comune din două cuvinte.

**Input:**
```python
cuv1 = "elefant"
cuv2 = "leu"
```

**Output:**
```python
Litere comune: {'e', 'l'}
```

---

### 1️⃣4️⃣ Divizori comuni
Afișează divizorii comuni a două numere.

**Input:**
```python
a = 12
b = 18
```

**Output:**
```python
Divizori comuni: {1, 2, 3, 6}
```

---

### 1️⃣5️⃣ Cuvinte unice ignorând majusculele
Normalizează textul și calculează câte cuvinte unice există.

**Input:**
```python
text = "Ana are Mere si mere"
```

**Output:**
```python
Cuvinte unice (lowercase): {'ana', 'are', 'mere', 'si'}
Total: 4
```

---

## 🔵 Nivel 4 – Complex

### 1️⃣6️⃣ Litere lipsă din alfabet
Afișează literele din alfabet care nu apar în text.

**Input:**
```python
text = "the quick brown fox"
```

**Output:**
```python
Litere lipsă: {'a', 'd', 'g', 'j', 'l', 'm', 'p', 's', 'v', 'y', 'z'}
```

---

### 1️⃣7️⃣ Cuvinte care apar doar într-una dintre două propoziții
Folosește diferența simetrică între seturi.

**Input:**
```python
p1 = "ana are mere"
p2 = "ion are pere"
```

**Output:**
```python
Cuvinte diferite: {'ana', 'ion', 'mere', 'pere'}
```

---

### 1️⃣8️⃣ Numere unice într-o matrice
Extrage toate numerele distincte dintr-o matrice (listă de liste).

**Input:**
```python
matrice = [[1, 2, 3], [2, 3, 4], [4, 5]]
```

**Output:**
```python
Numere unice: {1, 2, 3, 4, 5}
```

---

### 1️⃣9️⃣ Verificare anagrame
Verifică dacă două cuvinte sunt anagrame (au aceleași litere).

**Input:**
```python
cuv1 = "listen"
cuv2 = "silent"
```

**Output:**
```python
Sunt anagrame: True
```

---

### 2️⃣0️⃣ Unificarea datelor din mai multe surse
Găsește ID-urile comune și unice între trei liste.

**Input:**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5}
C = {4, 5, 6}
```

**Output:**
```python
Comune tuturor: {4}
Apar în cel puțin unul: {1, 2, 3, 4, 5, 6}
Unice fiecărui set:
  A: {1, 2}
  B: set()
  C: {6}
```
