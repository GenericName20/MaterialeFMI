# Probleme cu dicționare

## 1. Contor de cuvinte
**Enunț:** Scrie un program care numără de câte ori apare fiecare cuvânt într-un text folosind un dicționar.

**Input:**
```
Ana se duce la piata dimineata. Ana are foarte multa energie dimineata. Piata se deschide abia la 8.
```

**Output:**
```
'ana': 2
'se': 2
'duce': 1
'la': 2
'piata': 2
'dimineata': 2
...
```

---

## 2. Dicționar de studenți
**Enunț:** Creează un dicționar care stochează numele studenților și nota lor la un examen. Scrie funcții care:
- adaugă un student nou,
- actualizează nota unui student existent,
- calculează media notelor.

---

## 3. Dicționar de dicționare — frecvența literelor
**Enunț:** Dat un șir cu cuvinte separate prin spații, să se creeze un dicționar de forma `{cuvant: {litera: frecvența}}`.

**Input:**
```
sir = "teste programare teste"
```

**Output:**
```
{'teste': {'t': 4, 'e': 4, 's': 2},
 'programare': {'p': 1, 'r': 3, 'o': 1, 'g': 1, 'a': 2, 'm': 1, 'e': 1}}
```

---

## 4. Dicționar de divizori
**Enunț:** Se dă o listă de numere naturale. Să se creeze un dicționar `{numar: (divizorii_lui_proprii)}`.

**Input:**
```
nums = [50, 21, 13, 84, 50, 60]
```

**Output:**
```
{50: (2, 5, 10, 25),
 21: (3, 7),
 13: (),
 84: (2, 3, 4, 6, 7, 12, 14, 21, 28, 42),
 60: (2, 3, 4, 5, 6, 10, 12, 15, 20, 30)}
```

---

## 5. Frecvențe în liste — dicționar `{numar: [(indice, frecventa)]}`
**Enunț:** Se dă un set de numere și un tuplu de liste. Pentru fiecare număr din set, se creează o listă de tupluri care indică în ce listă apare și de câte ori.

**Input:**
```
nums1 = {10, 20, 14}
nums2 = ([10, 11, 10], [20, 20, 40], [5], [10, 11])
```

**Output:**
```
{10: [(0, 2), (3, 1)],
 20: [(1, 2)],
 14: []}
```

---

## 6. Dicționar după media cifrelor
**Enunț:** Se dă o listă de numere. Să se creeze un dicționar `{medie: [numere]}`, unde *numere* sunt cele care au media cifrelor egală cu cheia. Listele sunt sortate descrescător.

**Input:**
```
nums = [82375, 201, 51, 73, 3456, 2855, 1021, 90, 153]
```

**Output:**
```
{5.0: [82375, 2855, 73],
 1.0: [1021, 201],
 3.0: [153, 51],
 4.5: [3456, 90]}
```

---

## 7. Dicționar cu frecvența cifrelor pe număr
**Enunț:** Se creează un dicționar `{numar: [(cifra, frecventa)]}` pentru fiecare număr.

**Input:**
```
nums = [1011, 234, 8158558, 234]
```

**Output:**
```
{1011: [(1, 3), (0, 1)],
 234: [(3, 1), (4, 1), (2, 1)],
 8158558: [(1, 1), (8, 3), (5, 3)]}
```

---

## 8. Palindroame — vocale sau consoane
**Enunț:** Dintr-un șir se extrag palindroamele. Dacă numărul vocalelor ≥ consoanelor, se stochează vocalele (fără duplicate), altfel consoanele.

**Input:**
```
sir = "asa merem palindrom "
```

**Output:**
```
{'asa': ['a'],
 'merem': ['m', 'r']}
```

---

## 9. Frecvența relativă a literelor (din fișier)
**Enunț:** Fișierul `text.in` conține propoziții. Să se scrie în `text.out` literele și frecvențele lor relative.

**Input (`text.in`):**
```
Ana are multe pere si mere,
dar are mai multe mere
decat pere si prune
mai multe decat pere.
```

**Output (`text.out`):**
```
a: 0.125
n: 0.028
r: 0.125
e: 0.250
m: 0.097
u: 0.056
l: 0.042
t: 0.069
p: 0.056
s: 0.028
i: 0.056
d: 0.042
c: 0.028
```

---

## 10. Procesare fișier cu subliste
**Enunț:**  
1. Se citesc listele de numere din `numere.in`.  
2. Se elimină toate aparițiile minimului din fiecare sublistă.  
3. Se păstrează doar primele N elemente, unde N este lungimea minimă a sublistelor rămase.  
4. Rezultatul se scrie în `numere.out`.

**Input (`numere.in`):**
```
100 54 101 54 2 81 92
10 1 1 2 2 1 70
12 81 10 8 9 8 10
```

**Output (`numere.out`):**
```
100 54 101 54
10 2 2 70
12 81 10 9
```

---

