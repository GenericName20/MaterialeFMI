# Programarea Algoritmilor – Tutoriat 1


## 1. Introducere în Python
 Ce este Python?

Limbaj interpretat, multi-paradigmă (procedural, orientat obiect, funcțional).


### *Instalare*

🔗 [Python.org – Download](https://www.python.org/downloads/)


## 2. Tipuri de date fundamentale
| Tip de date | Clasă internă | Exemple | Descriere |
|--------------|----------------|-----------|------------|
| `NoneType` | `NoneType` | `None` | absența unei valori sau inițializarea unui parametru al unei funcții cu o valoare implicită |
| `int` | `int` | `5`, `0b101`, `0x1F` | numere întregi |
| `float` | `float` | `3.14`, `-2.5e3` | numere reale |
| `complex` | `complex` | `2+3j` | numere complexe |
| `bool` | `bool` | `True`, `False` | valori logice |
| `str` | `str` | `'text'`, `"abc"` | șiruri de caractere |
| `list` | `list` | `[1, 2, 3]` | secvență mutabilă |
| `tuple` | `tuple` | `(1, 2, 3)` | secvență imutabilă |
| `set` | `set` | `{1, 2, 3}` | mulțime fără duplicate |
| `dict` | `dict` | `{"a": 1, "b": 2}` | perechi cheie: valoare |



### **Tipuri**:

-Tipul NoneType 

-Tipuri numerice: int, float, complex

-Tipul boolean

-Tipuri secvențiale: șiruri de caractere, liste, tupluri

-Tipuri mulțime: set, frozenset

-Tablouri asociative: dict

## 3. Variabile și conversii

Python nu cere declararea tipului – tipul este determinat dinamic (care poate fi modificat ulterior).

Poți folosi funcțiile type() și id() pentru a inspecta o variabilă.

```python
a = 10
b = "10"
print(type(a), type(b))  # <class 'int'> <class 'str'>
print(int(b) + 5)        # conversie string -> int
```



## 4. Afișare și citire

### *Afișare*
```python
print("Salut", "Python", sep=" | ", end="!!!\n")
#print("Tutoariat")
```



### f-strings (format modern)
```python
nume = "Ana"
varsta = 20
print(f"{nume} are {varsta} ani.")
```



### *Citire*
```python
x= input("x= ")  //valoarea cititită este întodeauna un șir de caractere
```

   ! Pentru a transforma șirurile de caractere citite în valori de alte tipuri primitive se 
folosesc funcțiile de conversie int(șir), float(șir), complex(șir) sau bool(șir).

```python
n = int(input("Introdu un număr: "))
print(f"Pătratul lui {n} este {n**2}")
```


## 5. Operatorii principali
### -Aritmetici

* `+` : Adunare
* `-` : Scădere
* `*` : Înmulțire
* `/` : Împărțire (rezultat real/float)
* `//` : Împărțire întreagă (rezultat întreg)
* `%` : Modulo (restul împărțirii)
* `**` : Exponențiere (ridicare la putere)

```python
a, b = 7, 2
print(a / b, a // b, a % b, a ** b)
```

### -Relaționali

* `<` : Mai mic decât
* `<=` : Mai mic sau egal cu
* `>` : Mai mare decât
* `>=` : Mai mare sau egal cu
* `==` : **Egalitate** (Verifică dacă **valorile** sunt egale)
* `!=` : Diferit de
* `is` : **Identitate** (Testează dacă două variabile/expresii sunt identice)
* `is not` : Identitate negativă (Testează dacă două variabile/expresii **nu** sunt identice)
* `in` : **Apartenență** (Verifică dacă o valoare există într-o secvență)
* `not in` : Apartenență negativă (Verifică dacă o valoare nu există într-o secvență)

```python
# Verificarea prezenței într-o Listă
numere = [1, 2, 3]
print(3 in numere)      # True
print(5 not in numere)  # True

# Verificarea prezenței într-un Șir de Caractere (String)
cuvant = "Python"
print("y" in cuvant)    # True
print("oana" not in cuvant) # True
```

### -Logici

* `not` (Negație logică). Inversează valoarea booleană (schimbă `True` în `False` și invers).
* `and` (Conjuncție logică). Returnează `True` doar dacă **ambele** condiții sunt `True`.
* `or` (Disjuncție logică). Returnează `True` dacă **cel puțin una** dintre condiții este `True`.

```python
x = 0
print(not x)  # True (0 e considerat False)
```

### -Pe biți

| Operator | Descriere | Explicație |
| :------: | :-------: | :---------------: |
| `~` | **NOT pe biți** | Inversează toți biții (0 devine 1, 1 devine 0). Rezultatul folosește complementul față de doi (va fi negativ). |
| `&` | **AND pe biți** | Setează bitul la 1 dacă **ambii biți** corespunzători sunt 1. |
| `\|` | **OR pe biți**  | Setează bitul la 1 dacă **cel puțin unul** dintre biții corespunzători este 1. |
| `^` | **XOR pe biți** | Setează bitul la 1 dacă biții corespunzători sunt **diferiți**. |
| `<<` | **Deplasare la stânga** | Decalează biții spre stânga cu $n$ poziții (echivalent cu înmulțirea cu $2^n$). |
| `>>` | **Deplasare la dreapta** | Decalează biții spre dreapta cu $n$ poziții (echivalent cu împărțirea la $2^n$ și rotunjire în jos). |


```python
# Reprezentarea binară (pe 4 biți):
# 5  este: 0101
# 3  este: 0011

# 1. AND pe biți (&)
# 0101 & 0011 = 0001 (1 zecimal)
print(f"5 & 3 = {5 & 3}")

# 2. OR pe biți (|)
# 0101 | 0011 = 0111 (7 zecimal)
print(f"5 | 3 = {5 | 3}")

# 3. XOR pe biți (^)
# 0101 ^ 0011 = 0110 (6 zecimal)
print(f"5 ^ 3 = {5 ^ 3}")

# 4. Deplasare la stânga (<<)
# 5 << 1 (0101 decalat cu 1) = 1010 (10 zecimal)
print(f"5 << 1 = {5 << 1}")
```

### Operatorul condițional

*valoare_daca_true if conditie else valoare_daca_false*

```python
# Exemplu: Testarea parității unui număr
x = 7

# Dacă restul împărțirii lui x la 2 este 0, este "par". Altfel, este "impar".
rezultat = "par" if x % 2 == 0 else "impar"
```


## 6. Instrucțiuni de control
### -Atribuire

```python
x = 5
x += 3
a, b = 1, 2
a, b = b, a  # interschimbare
```

### -Condiționale (if, elif, else)

```python
x = int(input("x = "))
if x < 0:
    print("Negativ")
elif x == 0:
    print("Zero")
else:
    print("Pozitiv")
```


### -Repetiții (while, for)

### *Buclă while*

```python
n = 123
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Suma cifrelor =", s)
```


### *Buclă for*

### -Range personalizat

```python
for i in range(2, 10, 2):  # start=2, stop=10, pas=2 - strat inclusiv, stop exclusiv
    print(i)
```

```python
# 1. Iterare cu range() - start, stop, step
print("Numere de la 5 la 1 (descrescător):")
for i in range(5, 0, -1):
    print(i, end=" ")
# Output: 5 4 3 2 1

# 2. Iterare prin elementele unei liste
lista_culori = ["roșu", "verde", "albastru"]
print("\n\nCulorile sunt:")
for culoare in lista_culori:
    print(f"- {culoare}")

# 3. Iterare prin Dicționar (Chei și Valori)
note = {"Mate": 9, "Info": 10}
print("\nNotele:")
for materie, nota in note.items():
    print(f"La {materie}: {nota}")
```


## Alte instrucțiuni utile

continue → sare peste iterația curentă

break → oprește complet bucla

else → se execută doar dacă bucla s-a terminat natural

pass → “placeholder” fără acțiune ( nu are niciun efect în program )

```python
for i in range(10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)
else:
    print("Bucla s-a terminat normal.")
```

# 7.SIRURI DE CARACTERE  (str)

 Un șir de caractere este o secvență de caractere indexată de la 0, stocată ca un obiect de tipul clasei str.

### 7.1. Moduri de Reprezentare a Șirurilor

Constantele (literalii) de tip șir pot fi reprezentate în două moduri:

 'șir' sau "șir" - **O singură linie** (caracterele newline sunt ignorate)

 ```python
sir_1 = "Acesta este, de fapt,\nun sir scris\npe o singură linie!"

print(sir_1)
```

 '''șir''' sau """șir""" - **Mai multe linii** (caracterele newline nu sunt ignorate).
 
 ```python
sir_2 = """Acesta este
un sir scris
pe mai multe linii!"""

print(sir_2)
```

### 7.2. Imutabilitatea Șirurilor

Șirurile de caractere sunt imutabile. Aceasta înseamnă că:

-Valoarea unui obiect de tip str nu mai poate fi modificată după crearea sa.

-Nicio metodă din clasa str nu modifică șirul curent; în schimb, metodele creează și returnează un nou șir care conține rezultatul prelucrării.

```python
#Dacă vrei să transformi un șir în litere mari, trebuie să modifici referința variabilei
s = "test"
s.upper() # Metoda creează șirul "TEST", dar variabila s rămâne neschimbată
print(s)  # Output: test

# Corect: Reatribuirea noii referințe
s = s.upper() # s primește acum referința noului șir "TEST" 
print(s)  # Output: TEST
```

### 7.3. String Interning (Bazinul de Șiruri)

Python utilizează mecanismul de **string interning** pentru stocarea șirurilor, păstrând o singură copie a fiecărui șir distinct într-un **bazin de șiruri** (*string pool*).

* **Avantaje:** Reduce spațiul de memorie și crește viteza de comparare. Compararea `s == t` (valoare) poate fi înlocuită cu compararea `s is t` (referință/ID) care are complexitate $O(1)$ în loc de $O(len(s))$.
* **Se bazează pe imutabilitate**.
* **Internare Explicită:** Se poate folosi metoda `sys.intern(șir)` din modulul `sys` pentru a salva explicit un șir în bazin.



### 7.4 Accesarea și Secționarea (Slicing) String-urilor

#### Indexare
Elementele se accesează prin indici.

* **Indici pozitivi:** De la $0$ la $n-1$ (de la stânga la dreapta).
* **Indici negativi:** De la $-n$ la $-1$ (de la stânga la dreapta).
* **Atenție:** Accesarea este de tip *read-only* (doar în citire) din cauza imutabilității.

Șirurile de caractere sunt secvențe indexate de la **0** și sunt parcurse folosind indici sau intervale (slice-uri).

| Sintaxă | Descriere | Exemplu (`s = "Python"`) | Rezultat |
| :---: | :---: | :---: | :---: |
| `s[i]` | Acces prin **indice pozitiv** (de la 0). | `s[0]` | `'P'` |
| `s[-i]` | Acces prin **indice negativ** (de la -1, de la sfârșit). | `s[-1]` | `'n'` |
| `s[st:dr]` | **Slice** de la `st` (inclusiv) până la `dr` (**exclusiv**). | `s[1:4]` | `"yth"` |
| `s[:dr]` | De la început până la `dr` (**exclusiv**). | `s[:2]` | `"Py"` |
| `s[st:]` | De la `st` (inclusiv) până la sfârșit. | `s[3:]` | `"hon"` |
| `s[::pas]` | **Slice cu pas**. | `s[::-1]` | `"nohtyP"` |


### 7.5. Operatori Utili

| Operator | Descriere | Exemplu |
| :--- | :--- | :--- |
| `+` | Concatenare | `"un" + " exemplu"` = `"un exemplu"` |
| `*` | Multiplicare (concatenare repetată) | `"test" * 3` = `"testtesttest"` |
| `in`, `not in` | Testarea apartenenței unui subșir | `"est" in "atestat"` = `True` |
| `<`, `<=`, `>`, `>=`, `==`, `!=` | Comparări lexicografice (alfabetice) | `"POPA" == "Popa"` = `False` (depinde de implementare/locale) / **Atenție:** Literele mari sunt considerate "mai mici" lexicografic decât cele mici |



##  7.6.Metode utile  

| Categorie | Metodă | Descriere |
| :--- | :--- | :--- |
| **Transformare** | `lower()`, `upper()`, `swapcase()`, `title()`, `capitalize()` | Transformări de litere (ex: mici în mari, prima literă a fiecărui cuvânt mare, etc.) |
| **Formatare** | `strip([caractere])` | Elimină prefixul și sufixul formate din caractere indicate (sau spații albe, implicit) |
| | `center(lățime, [caracter])` | Centrează șirul într-o lățime dată, folosind un caracter de umplere (sau spații, implicit) |
| | `format(...)` | Înlocuiește câmpurile variabile (`{}`) cu parametrii metodei (secvențial, pozițional sau cu nume) |
| **Clasificare** | `isspace()`, `islower()`, `isupper()`, `isalpha()`, `isdigit()`, `isalnum()`, etc. | Verifică dacă toate caracterele sunt de un anumit tip (returnează `True`/`False`) |
| **Căutare** | `count(subșir, [start], [stop])` | Numără aparițiile disjuncte ale unui subșir |
| | `find(subșir, [start], [stop])` | Furnizează cel mai mic indice la care începe subșirul (sau -1) |
| | `rfind(subșir, [start], [stop])` | Furnizează cel mai mare indice la care începe subșirul (sau -1) |
| | `startswith(prefix, [start], [stop])` | Verifică dacă șirul începe cu prefixul dat |
| | `endswith(sufix, [start], [stop])` | Verifică dacă șirul se termină cu sufixul dat |
| | `replace(subșir, subșir_nou, [max])` | Înlocuiește aparițiile subșirului |
| **Divizare/Construire** | `split(separator)` | Furnizează o listă de subșiruri folosind separatorul (implicit: spații albe) |
| | `join(listă_subșiruri)` | Concatenează șubșirurile dintr-o listă, folosind șirul curent ca separator |

---

## 8. Manipularea Fișierelor Text

Un fișier text este o secvență de caractere stocată pe linii în memoria externă, asigurând **persistența datelor**.

### 8.1. Deschiderea unui Fișier

Funcția `open("cale fișier", ["mod de deschidere"])` asociază fișierul fizic cu un obiect la nivel logic (de obicei, `io.TextIOWrapper`).

| Mod | Descriere | Acțiuni în caz de fișier inexistent |
| :--- | :--- | :--- |
| `"r"` | Citire (read) - **Mod implicit** | Generează `FileNotFoundError` |
| `"w"` | Scrierea (write) | Creează unul nou; dacă există, îl șterge automat și îl înlocuiește |
| `"x"` | Scrierea exclusivă (exclusive write) | Creează unul nou; dacă există, generează `FileExistsError` |
| `"a"` | Adăugare (append) | Creează unul nou; dacă există, scrie după ultimul caracter |

* **Tratarea excepțiilor:** Se folosește o structură `try...except` pentru a gestiona erorile de tip `FileNotFoundError` sau `FileExistsError`.

### 8.2. Citirea Datelor

Datele citite dintr-un fișier text sunt întotdeauna furnizate ca **șiruri de caractere**.

| Metodă | Descriere | Notă |
| :--- | :--- | :--- |
| `read()` | Furnizează **tot conținutul** fișierului text într-un singur șir de caractere. | Șirul returnat conține și caracterele de delimitare a liniilor (`\n`). |
| `readline()` | Furnizează conținutul **liniei curente** ca șir, sau un șir vid la sfârșitul fișierului. | Șirul returnat conține și caracterul de linie nouă (`\n`). |
| `readlines()` | Furnizează **toate liniile** într-o listă de șiruri de caractere. | Fiecare șir din listă conține și caracterul de linie nouă (`\n`). |

* **Citirea eficientă:** Pentru fișiere mari, se preferă citirea linie cu linie (iterarea directă a obiectului fișier) pentru a economisi memorie.
* **Conversia la Numere:** Dacă doriți să citiți numere, trebuie folosită o funcție de conversie, de exemplu `int()`.

### 8.3. Scrierea Datelor

Într-un fișier text se pot scrie **doar șiruri de caractere**.

| Metodă | Descriere |
| :--- | :--- |
| `write(șir)` | Scrie șirul în fișier, **fără a adăuga automat o linie nouă**. |
| `writelines(colecție de șiruri)` | Scrie toate șirurile din colecție, **fără a adăuga linii noi între ele**. |

### 8.4. Închiderea Fișierului

Fișierul trebuie închis explicit cu metoda `close()`.

* **Risc:** Dacă un fișier deschis pentru scriere nu este închis, ultimele informații scrise s-ar putea să nu fie salvate.
* **Instrucțiunea `with...as`:** Elimină necesitatea închiderii explicite, asigurând închiderea automată a fișierului chiar și în caz de erori.

```python
with open("exemplu.txt") as f:
    # Prelucrarea fișierului
    s = f.readlines()
# Aici fișierul f este deja închis automat
```


## 9. Probleme 

1️⃣ Paritate
```python
n = int(input("n = "))
print("Par" if n % 2 == 0 else "Impar")
```


2️⃣ Maximul dintre 3 numere
```python
a, b, c = map(int, input("a b c = ").split())
print("Maximul este", max(a, b, c))
```


3️⃣ Factorial
```python
n = int(input("n = "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f"{n}! = {f}")
```


4️⃣ Număr prim
```python
n = int(input("n = "))
for d in range(2, n // 2 + 1):
    if n % d == 0:
        print("Nu e prim")
        break
else:
    print("Este prim")
```


5️⃣ Suma numerelor pozitive până la 0
```python
s = 0
while True:
    x = int(input("x = "))
    if x == 0:
        break
    s += x
print("Suma =", s)
```
