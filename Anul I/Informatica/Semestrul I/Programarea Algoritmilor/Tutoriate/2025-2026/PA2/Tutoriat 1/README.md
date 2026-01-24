# 🐍 Tutoriat 1 — De ce Python?

> „Înainte să învățăm algoritmi, hai să vedem **de ce merită să îi scriem în Python**.”

---

## 🧠 1. De ce Python?

Python e unul dintre cele mai folosite limbaje din lume.  
E simplu, expresiv și are o comunitate uriașă - cu **foarte multe librării pentru diverse domenii** și **o mulțime de materiale de învățare**. 
Scrii mai puțin cod => înțelegi mai mult ce se întâmplă => poți gândi mai mult la **algoritm**, nu la **sintaxă**.

Exemplu clasic:
```python
# C++ style
for (int i = 0; i < 10; i++) cout << i << endl;

# Python style
for i in range(10):
    print(i) 
```


---

## 🧩 2. Cu ce se leagă din facultate?

- **Programare** - logică, structuri de date  
- **Algoritmică** - accent pe gândire, nu pe limbaj  
- **LFA (Limbaje Formale și Automate)** - implementarea automatelor e mult mai ușoară în Python, mai ales datorită manipulării simple a stringurilor și colecțiilor  
- **Probabilități și Statistică (anul 2)** - unele serii folosesc Python pentru simulări și generare de distribuții la laborator  
- **Algoritmi Fundamentali** - se poate alege între C++ și Python pentru implementarea cerințelor  
- **Inteligență Artificială**, **Machine Learning** - 90 % se face în Python   
- **Web** - `django`, (opțional posibil în anul 2)  


---

## 💼 3. La ce ajută pe plan profesional?

- Teste tehnice în firme mari (Google, Meta, Amazon) - Python e limbaj standard de interviu + te lasă să te concentrezi mai mult pe problemă, nu pe sintaxă
- **Machine Learning / Data Science** - ecosistem Pythonic 
- **Backend development** - rapid de prototipat  
- **Scripting & automation** - ușurează viața oricăruia din noi :) 

---


## 🧱 4. Structurile de date de bază în Python

| Tip | Descriere | Exemplu |
|-----|------------|----------|
| `list` | colecție ordonată, mutabilă | `[1, 2, 3]` |
| `tuple` | colecție ordonată, nemodificabilă | `(1, 2, 3)` |
| `set` | colecție neordonată, unică | `{1, 2, 3}` |
| `dict` | perechi cheie–valoare | `{'nume': 'Ana', 'vârstă': 20}` |
| `str` | șir de caractere | `"Python"` |

---

## ⚙️ 5. Ce are Python și nu au celelalte limbaje

- Indentare - cod curat și lizibil  
- Tipuri dinamice - poți schimba tipurile rapid  
- Garbage collector automat  
- Biblioteci imense (`numpy`, `pandas`, `matplotlib`, `requests`, etc.)  
- Interactivitate - rulezi direct în terminal, fără compilare  

---

## 🔁 6. Reminder: intervale în `for` și indexare

`range(a, b)` - generează valori în **[a, b)**, adică **inclusiv a, exclusiv b**.  
Exemplu:  
```
for i in range(3): print(i)
```
Indexare:  
```
s = "python"  
print(s[0]) # indexare de la 0 => p
print(s[-1]) # indici negativi = luati de la final => n
```
---

## ⚡ 7. Compilat vs. Interpretat

| Tip | Exemple | Cum rulează |
|------|----------|-------------|
| Compilat | C, C++ | cod - compilator - binar executabil |
| Interpretat | Python, JavaScript | cod - interpretor - rulează linie cu linie |

Python *nu* creează un executabil direct, ci îl **interpretează** linie cu linie.

💡 Dacă avem o eroare într-un `if` în care **nu se ajunge niciodată**, Python nu o va semnala la rulare, pentru că acel cod **nu este executat**.  
Într-un limbaj compilat (ex: C++), eroarea ar fi prinsă încă din faza de compilare, chiar dacă ramura respectivă nu se execută.

Exemplu:  
```
if False:  
  print(x + "test")  # eroare de tip, dar nu se execută => Python nu se plânge  
```

---

## 🧹 8. Garbage collector & variabile care împart memoria

Python gestionează memoria automat.  
Dacă două variabile indică spre același obiect:  
```
a = [1, 2, 3]  
b = a  
b.append(4)  
print(a)
```
ambele referă **același obiect în memorie**.  

Garbage collector-ul șterge automat obiectele nefolosite (fără referințe active).

---

## 🧬 9. Strongly & Dynamically Typed

- **Strongly typed** - nu face conversii implicite ciudate  
- **Dynamically typed** - nu specifici tipurile dinainte  

Exemplu:  
```
x = 5  
x = "cinci"
```
Python este **strongly & dynamically typed**:  
tipurile contează, dar nu trebuie declarate explicit.

---

## 🎯 10. Concluzie

Python = rapid, expresiv și perfect pentru a te concentra pe **algoritmi**, nu pe **sintaxă**.  
Și da — faptul că îl învățăm din anul I ne face printre cei mai faini studenți din țară. 🚀  

---

## ❓ 11. Questions?

### 🔸 Ce e `None`?
`None` este un **obiect special** care reprezintă absența unei valori.  
Echivalentul lui `NULL` din alte limbaje.  
Orice funcție care nu are `return` explicit întoarce automat `None`.

---

### 🔸 De ce nu există `++i`?
Python **nu are operatori de incrementare/decrementare** (`++`, `--`)  
pentru că valorile numerice sunt **imutabile** — adică nu pot fi modificate „în loc”.  
Operația `i += 1` creează de fapt **un nou obiect numeric**, nu modifică vechiul `i`.

---

### 🔸 Cum e reprezentată memoria în spate?
Toate variabilele în Python sunt **referințe către obiecte**.  
Memoria este gestionată automat prin **garbage collector**,  
iar obiectele sunt stocate pe heap.  
Dacă două variabile indică același obiect, modificarea printr-una se vede și prin cealaltă  
(dacă obiectul este mutabil, ex: listă sau dicționar).

---

### 🔸 Ce diferență e între `is` și `==`?
- `==` verifică **egalitatea valorilor** (conținutul e același)  
- `is` verifică **identitatea obiectului** (dacă sunt exact același obiect în memorie)

Exemplu:  
```
a = [1, 2, 3]  
b = [1, 2, 3]  
c = a  
```

a == b  => True (au același conținut)  
a is b  => False (sunt obiecte diferite)  
a is c  => True (referă exact același obiect în memorie)



👨‍🏫 **Următorul tutoriat:** Liste, string-uri și comprehensiuni.

