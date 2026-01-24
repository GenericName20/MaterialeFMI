# Programare Dinamică



## 1. Ce este Programarea Dinamică

**Programarea Dinamică (DP)** este o tehnică de rezolvare a problemelor de **optimizare**, care constă în:
- împărțirea problemei în **subprobleme mai mici**
- rezolvarea fiecărei subprobleme **o singură dată**
- memorarea soluțiilor și **reutilizarea lor**

Scopul principal al Programării Dinamice este evitarea **recalculărilor inutile** care apar în soluțiile brute (de obicei recursive).

---

## 2. Când putem folosi Programarea Dinamică

O problemă poate fi rezolvată cu Programare Dinamică **doar dacă** sunt îndeplinite **ambele condiții**:

### 🔹 Substructură optimală
Soluția optimă globală se obține din soluțiile optime ale subproblemelor.

### 🔹 Subprobleme suprapuse
Aceleași subprobleme apar de mai multe ori în rezolvarea naivă (recursivă).

Dacă una dintre aceste condiții nu este îndeplinită, Programarea Dinamică **nu este justificată**.

---

## 3. DP vs Greedy vs Backtracking

| Metodă | Corectitudine | Complexitate |
|------|---------------|--------------|
| Greedy | ❌ nu mereu | mică |
| Backtracking | ✅ mereu | ❌ exponențială |
| **Programare Dinamică** | ✅ mereu | ✅ eficientă |

Programarea Dinamică este **cea mai sigură metodă** pentru problemele de optimizare.

---

## 4. Pașii standard în Programarea Dinamică

Pentru a rezolva o problemă cu DP:

1. Identificăm **subproblemele**
2. Definim **relația de recurență**
3. Alegem o **structură de memorare** (vector / matrice)
4. Calculăm soluțiile **bottom-up**
5. (Opțional) **Reconstituim soluția optimă**

---

## 5. Exemplu introductiv: Șirul lui Fibonacci

### Enunț
Să se determine al `n`-lea termen din șirul lui Fibonacci:
- `F(1) = 0`
- `F(2) = 1`
- `F(n) = F(n-1) + F(n-2)`, pentru `n ≥ 3`

---

### Varianta recursivă (ineficientă)

```python
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
```
❌ Această variantă recalculează aceleași valori de mai multe ori  
❌ Are complexitate **exponențială**

---

### Varianta cu Programare Dinamică (Bottom-up)

```python
def fib(n):
    f = [-1, 0, 1]
    for i in range(3, n+1):
        f.append(f[i-2] + f[i-1])
    return f[n]
```
### Explicație

Această soluție utilizează **Programarea Dinamică în varianta bottom-up**, ceea ce înseamnă că soluția este construită progresiv, pornind de la cele mai simple subprobleme.

Principalele idei ale abordării sunt:
- se evită complet recursivitatea  
- fiecare subproblemă este rezolvată o singură dată  
- rezultatele sunt memorate și reutilizate  

Prin această abordare sunt eliminate recalculările inutile prezente în varianta recursivă.

---

### Structura de memorare

Se folosește un vector `f`, care joacă rolul de **tabel de Programare Dinamică**.

Semnificația elementelor:
- `f[i]` reprezintă valoarea termenului Fibonacci `F(i)`

Inițializare:
- `f[1] = 0`
- `f[2] = 1`

Aceste valori reprezintă **cazurile de bază** ale problemei.

---

### Relația de recurență

Problema este definită matematic prin relația:

```text
F(n) = F(n - 1) + F(n - 2)
```
Această relație evidențiază **substructura optimală**, deoarece soluția pentru `n`
depinde exclusiv de soluțiile pentru valori mai mici.

---

### Ordinea de calcul

Valorile sunt calculate în ordine crescătoare:
- mai întâi cazurile de bază
- apoi `F(3), F(4), ..., F(n)`

Această ordine este caracteristică metodei **bottom-up** și este recomandată la examen.

---

### Complexitate

- **Complexitate în timp:** `O(n)`
- **Complexitate în memorie:** `O(n)`

Comparativ:

| Metodă | Complexitate |
|------|--------------|
| Recursivă simplă | ❌ Exponențial |
| Programare Dinamică | ✅ O(n) |

---

## Gândirea din spate pentru Programarea Dinamică

Pentru a rezolva corect o problemă folosind Programare Dinamică, trebuie urmați următorii pași:

---

### 1. Identificarea subproblemelor

Se determină cele mai mici versiuni ale problemei care pot fi rezolvate direct.

**Exemplu:**  
Pentru Fibonacci, subproblemele sunt `F(n-1)` și `F(n-2)`.


### 2. Definirea relației de recurență

Se stabilește modul în care soluția curentă se obține din soluțiile subproblemelor.

**Exemplu:**

```text
F(n) = F(n - 1) + F(n - 2)
```

### 3. Alegerea structurii de memorare

Se alege o structură de date pentru memorarea rezultatelor, în funcție de natura problemei:

- **vector** – pentru probleme unidimensionale  
- **matrice** – pentru probleme bidimensionale  

Structura aleasă trebuie să permită acces rapid la soluțiile subproblemelor.


### 4. Stabilirea ordinii de calcul

Soluțiile sunt calculate:
- de la subproblemele mici către problema inițială  
- folosind abordarea **bottom-up**

Această ordine asigură faptul că, atunci când calculăm o valoare, toate subproblemele de care depinde sunt deja rezolvate.


### 5. Construirea soluției finale

După completarea tabelului de Programare Dinamică:
- se poate afișa direct **valoarea optimă**
- sau se poate **reconstrui soluția optimă** folosind informații auxiliare (de exemplu, un vector de predecesori)

---


## Concluzie

Programarea Dinamică este o tehnică esențială pentru rezolvarea problemelor de optimizare.

Este recomandată atunci când:
- problema poate fi împărțită în subprobleme  
- subproblemele se suprapun  
- soluția optimă globală depinde de soluții locale  

Dacă o problemă cere:
- **maxim sau minim**  
- **număr de moduri**  
- **decizii succesive**  

=> **Programarea Dinamică este prima tehnică de luat în considerare.**


------

# Backtracking 

## Ce este Backtracking?

**Backtracking** este o tehnică de programare folosită pentru:
- generarea tuturor soluțiilor unei probleme
- evitarea explorării soluțiilor care sigur nu pot duce la un rezultat valid

 Ideea principală:
> Construim soluția **pas cu pas** și abandonăm imediat o soluție parțială
> dacă observăm că nu poate deveni soluție finală.

Astfel, evităm o rezolvare de tip **forță brută**.

---

## Noțiuni importante

- **Soluție parțială**  
  O soluție incompletă care respectă condițiile problemei până la acel moment.

- **Soluție finală**  
  O soluție parțială completă care îndeplinește toate condițiile.

- **Condiții de continuare**  
  Condiții care spun dacă are sens să mai extindem soluția curentă.

---

## Forma generală a unui algoritm Backtracking

```python
def back(k):
    for valoare in valori_posibile:
        sol[k] = valoare
        if solutie_partiala_valida(sol, k):
            if solutie_completa(sol, k):
                prelucreaza_solutia(sol)
            else:
                back(k + 1)
```

### Ideea generală

- `k` = poziția curentă în soluție  
- `sol` = soluția construită pas cu pas  

La fiecare pas:
- încercăm o valoare
- verificăm dacă soluția parțială este validă
- continuăm sau ne întoarcem (backtrack)

---

## Exemplul 1 – Generarea permutărilor (clasic)

**Problemă:**  
Generăm toate permutările mulțimii `{1, 2, ..., n}`.

**Condiție:**
- toate valorile trebuie să fie distincte

```python
def back(k):
    for v in range(1, n + 1):
        sol[k] = v
        if v not in sol[:k]:
            if k == n:
                print(*sol[1:])
            else:
                back(k + 1)

n = int(input())
sol = [0] * (n + 1)
back(1)
```

**Complexitate:** `O(n!)`  
(deoarece se afișează `n!` permutări)

---

## Exemplul 2 – Combinări (fără ordine)

**Problemă:**  
Generăm toate submulțimile cu `m` elemente din mulțimea `{1, 2, ..., n}`.

**Idee simplă:**
- generăm elementele în **ordine crescătoare**
- evităm duplicatele alegând fiecare element mai mare decât precedentul

```python
def back(k):
    for v in range(sol[k - 1] + 1, n + 1):
        sol[k] = v
        if k == m:
            print(*sol[1:])
        else:
            back(k + 1)

n = int(input())
m = int(input())
sol = [0] * (m + 1)
back(1)
```
---

## Exemplu 3 – Generarea codurilor PIN (Backtracking)

### Problema

Se dau două numere naturale:
- `n` – lungimea codului PIN
- `p` – numărul maxim de apariții ale unei cifre

Trebuie generate **toate codurile PIN** care respectă următoarele condiții:
- codul are exact `n` cifre
- cifrele sunt din intervalul `1..9`
- nu există două cifre alăturate egale
- fiecare cifră apare de **cel mult `p` ori**

La final se afișează și **numărul total de coduri** generate.

---

### Ideea de Backtracking

Construim codul cifră cu cifră:
- `sol` = codul construit până acum (soluție parțială)
- `cnt[d]` = de câte ori a fost folosită cifra `d`

La fiecare pas:
1. încercăm o cifră `d` între `1` și `9`
2. verificăm condițiile:
   - `d` ≠ ultima cifră din `sol`
   - `cnt[d] < p`
3. dacă este validă, continuăm recursiv
4. după revenire, refacem starea (backtrack)

---

### Cod Python 

```python
def back():
    # Solutie completa
    if len(sol) == n:
        print("".join(map(str, sol)))
        total[0] += 1
        return

    for d in range(1, 10):
        # Nu permitem doua cifre alaturate egale
        if sol and sol[-1] == d:
            continue

        # O cifra apare cel mult p ori
        if cnt[d] == p:
            continue

        # Alegem cifra d
        sol.append(d)
        cnt[d] += 1

        # Continuam constructia
        back()

        # Revenim (backtracking)
        cnt[d] -= 1
        sol.pop()


# Date de intrare
n, p = map(int, input().split())

sol = []
cnt = [0] * 10
total = [0]

back()

print("Numar total coduri:", total[0])
```

## Observații despre complexitate

- Algoritmii de tip **Backtracking** au, în general, **complexitate mare**.
- Timpul de execuție este proporțional cu:

> **numărul de soluții generate**

Cu cât există mai multe soluții valide, cu atât algoritmul va rula mai mult.

### Exemple uzuale de complexitate

- **Permutări** → `O(n!)`  
  (toate aranjamentele posibile ale celor `n` elemente)

- **Combinări** → `O(C(n, m))`  
  (numărul de submulțimi de `m` elemente din `n`)

- **Coduri PIN cu restricții** →  
  depinde de restricții (`n`, `p`, condiții pe vecinătate),  
  dar este **exponențial** în cel mai defavorabil caz.

---

## Avantaje și dezavantaje ale Backtracking-ului

### Avantaje
- ușor de implementat
- foarte clar logic
- permite generarea **tuturor soluțiilor**
- elimină rapid soluțiile imposibile

### Dezavantaje
- consum mare de timp
- nu este potrivit pentru valori mari ale lui `n`
- trebuie folosit doar când alte tehnici (Greedy / DP) nu se potrivesc

---

## Când folosim Backtracking?

✔ când trebuie să generăm **toate soluțiile**  
✔ când există **restricții clare**  
✔ când dimensiunea problemei este mică  

❌ nu se folosește pentru input mare  
❌ nu se folosește pentru optimizare simplă (unde DP e mai bun)

---

## Concluzie

Backtracking este o tehnică fundamentală în Programarea Algoritmilor care:

- construiește soluții **pas cu pas**
- verifică permanent validitatea soluțiilor parțiale
- elimină ramurile inutile din căutare
---

