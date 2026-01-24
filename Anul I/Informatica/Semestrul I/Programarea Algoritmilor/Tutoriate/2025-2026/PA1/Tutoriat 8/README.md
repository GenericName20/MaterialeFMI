# Tehnica Greedy

## 1. Ce este, de fapt, Greedy?

Tehnica **Greedy** (lacomă) este folosită la **probleme de optimizare** – adică atunci când ni se cere:
- minim
- maxim
- cel mai scurt
- cel mai ieftin

### Metaforă simplă

Imaginează-ți că ești un **alpinist** în ceață:
- La fiecare pas, alegi drumul care **urcă cel mai mult pe moment** (optim local).
- Speri că aceste alegeri te vor duce la **cel mai înalt vârf** (optim global).
- Problema: nu întotdeauna optimul local duce la optim global → te poți bloca pe un deal mai mic.


### Definiție simplă

> Greedy construiește soluția **pas cu pas**, alegând mereu cea mai bună opțiune disponibilă **în acel moment**, fără să revină asupra deciziilor.

---

## 2. Framework – Cum abordezi o problemă Greedy 

### Pasul 1 – Recunoaște tipul problemei

Dacă vezi cuvinte ca:
- „minim”
- „maxim”
- „cel mai mic”
- „cel mai mare”

=> Este o problemă de **optimizare**.

Formal:
> Cauți o submulțime `S ⊆ A` care optimizează o funcție obiectiv (min/max).

*functia obiectiv - criteriul matematic prin care măsurăm cât de "bună" este o soluție  => este formula pe care încercăm să o maximizăm (profit, număr de activități) sau să o minimizăm (cost, timp, distanță)



| Problema | Scopul (Min/Max) | Funcția Obiectiv (Ce măsurăm exact) |
| :--- | :---: | :--- |
| **Rucsacul Fracționar** | **Maximizare** | **Câștigul total:** $C(X) = \sum c_i x_i$ <br> *(unde c_i este câștigul și x_i este fracțiunea luată)* |
| **Planificarea Spectacolelor** <br> *(o singură sală)* | **Maximizare** | **Cardinalul submulțimii:** Numărul total de spectacole compatibile care pot fi planificate fără suprapuneri. |
| **Minimizarea Timpului de Așteptare** | **Minimizare** | **Timpul mediu de așteptare:** $M = \frac{\sum a_i}{n}$ <br> *(unde a_i este timpul de așteptare al persoanei i)* |
| **Planificarea Spectacolelor** <br> *(minim de săli)* | **Minimizare** | **Numărul de resurse:** Numărul minim de săli necesare astfel încât să nu existe suprapuneri în nicio sală. |
| **Submulțime de sumă maximă** | **Maximizare** | **Suma elementelor:** $f(S) = \sum_{x \in S} x$ <br> *(pentru o submulțime S(A)*  |
---

### Pasul 2 – Propune o regulă Greedy


De obicei implică:
- sortare
- selecție pas cu pas

Exemplu:
Vrei să cari cât mai multe cutii.
Poți încerca:
- cutiile cele mai ușoare primele
- cutiile cele mai mici ca volum

---

### Pasul 3 – Testează regula (contra-exemplu)

Încearcă să „strici” regula ta.

#### Exemplu clasic – Problema restului

Regulă: „ia moneda cu valoarea cea mai mare posibilă”

- Sistem: `{1, 3, 4}`
- Rest de dat: `6`

----

### Greedy

1. Ia 4 → rămâne 2  
2. Ia 1 → rămâne 1  
3. Ia 1 → rămâne 0  

Total: **3 monede (4+1+1)**

### Optim: 3 + 3  
Total: **2 monede**

### Concluzie: Greedy NU funcționează mereu.

---

### Pasul 4 – Demonstrație intuitivă (Exchange Argument)

Dacă nu găsești contra-exemplu:

Întreabă-te:
> „Dacă nu aleg această opțiune, pot obține ceva mai bun?”

**Exchange Argument**:
Presupui că există o soluție optimă diferită de Greedy și arăți că o poți transforma în soluția Greedy fără să pierzi calitatea.

---

## 3. Șablon de cod Greedy (Python)

Majoritatea algoritmilor Greedy arată așa:

```python
def solve_greedy(items):
    # 1. Prelucrare
    items.sort(key=lambda x: x.criteriu)  # reverse=True pentru descrescător

    solutie = []
    stare_curenta = 0

    # 2. Selecție
    for item in items:
        if conditie(item, stare_curenta):
            solutie.append(item)
            actualizeaza(stare_curenta, item)

    return solutie
```

## 4. Probleme clasice Greedy 

---

### A. Minimizarea timpului mediu de așteptare

**Scenariu:**   
Ai `n` persoane cu timpi de servire diferiți.

**Ideea Greedy:**   
Persoanele care au nevoie de mai puțin timp trebuie servite primele.

**Criteriu Greedy:**   
Sortezi **crescător** după timpul de servire.

**Exemplu:**

```text
Timpi:   [7, 6, 3]
Sortat:  [3, 6, 7]

Așteptări:
P1: 0
P2: 3
P3: 3 + 6 = 9

Total: 12
Medie: 4
```


### B. Programarea spectacolelor (o singură sală)

**Scenariu:**  
Ai mai multe evenimente, fiecare având un interval de timp `[start, finish)`.  
Vrei să selectezi **numărul maxim de spectacole** care nu se suprapun.

**Ideea Greedy:**  
Alegi evenimentele care se termină **cât mai repede**, pentru a lăsa loc altora.

**Criteriu Greedy:**  
Sortezi evenimentele **crescător după ora de final (`finish`)**.

**Strategii greșite (de ce nu funcționează):**
- „Spectacolul cel mai scurt” → poate fi scurt, dar plasat prost în timp.
- „Cel care începe primul” → poate dura toată ziua și bloca restul.

**Algoritm pas cu pas:**

```text
1. Sortează evenimentele după finish_time
2. Alege primul eveniment
3. Pentru fiecare eveniment următor:
   dacă start_time >= finish_time al ultimului ales → selectează-l
```

Exemplu
```text
Evenimente:
[8:00–10:00], [9:00–11:00], [10:00–12:00], [12:00–13:00]

Sortate după finish:
[8–10], [9–11], [10–12], [12–13]

Selectate:
[8–10], [10–12], [12–13]
```

### C. Număr minim de săli (Interval Partitioning)

**Scenariu:**  
Ai mai multe spectacole sau activități care trebuie să aibă loc toate. Vrei să afli numărul minim de săli necesare pentru a le programa fără suprapuneri.

**Ideea Greedy:**
Procesezi spectacolele cronologic. Pentru fiecare spectacol nou, verifici dacă s-a eliberat deja o sală. Dacă da, o ocupi pe aceea; dacă nu, ești obligat să deschizi o sală nouă.

**Criteriu Greedy:**
Sortezi evenimentele crescător după ora de **început**.  
*(Spre deosebire de problema anterioară unde sortam după final!)*

**Structură de date necesară:**
**Min-Heap (Priority Queue)** — această structură va reține orele de final ale sălilor ocupate. Ne permite să aflăm în `O(1)` care sală se eliberează cel mai repede.

---

### Algoritm pas cu pas
```plaintext
1. Sortează spectacolele după ora de început.
2. Inițializează un Min-Heap gol (pentru orele de final).
3. Adaugă primul spectacol în heap (ocupă prima sală).
4. Pentru fiecare spectacol următor:
   - Extrage minimul din heap (sala care se eliberează cel mai repede).
   - Dacă start_time_curent >= min_time_heap:
         Refolosești sala (actualizezi ora de final și o pui înapoi în heap).
   - Altfel:
         Creezi o sală nouă (pui ora de final a spectacolului curent în heap).
         (Și pui înapoi în heap sala pe care ai încercat să o iei, nemodificată).
```

Exemplu

```text
Spectacole: [9–11], [9–12], [11–13]

Heap (simulare):
1. Procesăm [9-11]: Heap = [11]       (O sală ocupată până la 11)
2. Procesăm [9-12]: 9 < 11.           (Nu e loc). Heap = [11, 12]
3. Procesăm [11-13]: 11 >= 11.        (E loc în sala 1). Heap = [12, 13]

Rezultat: 2 săli (dimensiunea heap-ului la final)
```


### D. Rucsacul fracționar (Fractional Knapsack)

**Scenariu:**  
Ai un rucsac cu o capacitate maximă `G` și o listă de obiecte, fiecare având o greutate `g` și o valoare `v`. Poți lua **fracțiuni** din obiecte (ex: aur praf, cereale).


**Ideea Greedy:**
Alegi obiectele care sunt cele mai "eficiente", adică oferă cea mai mare valoare pentru fiecare unitate de greutate ocupată.

**Criteriu Greedy:**
Calculezi pentru fiecare obiect câștigul unitar:  
```plaintext
raport = valoare / greutate
```

### Algoritm pas cu pas
```plaintext
1. Calculează raportul v/g pentru toate obiectele.
2. Sortează obiectele descrescător după raport.
3. Pentru fiecare obiect (cât timp mai ai loc):
   - Dacă obiectul încape complet:
         Ia-l pe tot.
         Scade greutatea lui din capacitatea rămasă.
   - Altfel (nu mai e loc pentru tot):
         Calculează cât spațiu a mai rămas.
         Ia doar fracțiunea care încape (spațiu_rămas / greutate_obiect).
         Oprește algoritmul (rucsacul e plin).
```
Exemplu

```text
Capacitate: 50

Obiecte:
A: g=10, v=60  → raport=6  (Locul 1)
B: g=20, v=100 → raport=5  (Locul 2)
C: g=30, v=120 → raport=4  (Locul 3)

Rezultat:
1. Iei A complet (10kg). Rămas: 40kg. Valoare: 60.
2. Iei B complet (20kg). Rămas: 20kg. Valoare: 60+100=160.
3. Iei fracțiune din C. Ai nevoie de 20kg, el are 30kg.
   Iei 20/30 (adică 2/3). Valoare: 2/3 * 120 = 80.
   Total final: 160 + 80 = 240.

```

#### Atenție: Dacă nu pot fi tăiate (0/1 knapsack), Greedy NU funcționează.


## 5. Cheat Sheet pentru examen

| Problemă                | Sortezi după        | Idee cheie                     | Complexitate   |
|-------------------------|------------------|--------------------------------|---------------|
| Sumă subset max          | valoare (>0)      | ia doar pozitivele            | O(n)          |
| Top K elemente           | valoare descrescător | primele K                    | O(n log n)    |
| Min waiting time         | timp crescător     | rapizii în față               | O(n log n)    |
| Max spectacole           | finish time       | eliberezi sala repede          | O(n log n)    |
| Min săli                 | start time        | heap                           | O(n log n)    |
| Rucsac fracționar        | v/g descrescător  | doar obiecte divizibile        | O(n log n)    |

---


