## PROBLEMA 1: Prelucrare Text

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Sunt formate exclusiv din litere mici (`a`–`z`).
* **Separatorii:** Sunt spațiul (` `) și setul de caractere: `.,!?:;-`.

---

##  Cerințe Funcționale ($T$)

Programul citește mai întâi valoarea $T$ și apoi textul. Rezultatul se afișează la ieșirea standard (consolă).

| $T$ | Sarcina de rezolvat | Ieșire la consolă |
| :---: | :--- | :--- |
| **1** | **Numărare și listare** | Numărul total de cuvinte, urmat de lista cuvintelor (câte unul pe rând). |
| **2** | **Cuvântul minim lexicografic** | Cuvântul care apare primul în ordine alfabetică. |
| **3** | **Căutare subșir** | Numărul de cuvinte care conțin secvența **`ini`**. |
| **4** | **Oglindire** | Fiecare cuvânt din text, afișat **inversat** (oglindit), câte unul pe rând. |
| **5** | **Terminație specifică** | Numărul de cuvinte care se termină cu litera **`a`**. |
| **6** | **Lungimi extreme** | Lungimea minimă urmată de lungimea maximă (separate printr-un spațiu). |

---

##  Restricții

* Lungimea textului $\leq 1000$ caractere.  
* Lungimea fiecărui cuvânt $\leq 50$ caractere.

---

##  Exemple

### Exemplul 1: $T = 1$ (Listare)

| Intrare | Ieșire |
| :--- | :--- |
| `1` <br> `...destul de rece? desigur!` | `4` <br> `destul` <br> `de` <br> `rece` <br> `desigur` |

### Exemplul 2: $T = 4$ (Oglindire)

| Intrare | Ieșire |
| :--- | :--- |
| `4` <br> `...destul de rece? desigur!` | `lutsed` <br> `ed` <br> `ecer` <br> `rugised` |

### Exemplul 3: $T = 6$ (Lungimi Min/Max)

| Intrare | Ieșire |
| :--- | :--- |
| `6` <br> `este frumoasa, desteapta si devreme acasa.` | `2 9` |

---

##  PROBLEMA 2: Cuvinte cu Lungimi Egale

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Sunt formate din litere mici (`a`–`z`).  
* **Separatorii:** Sunt spațiul (` `) și setul de caractere: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Găsirea perechii adiacente** | Se afișează primele două cuvinte consecutive cu aceeași lungime, separate printr-un spațiu. Dacă nu există, se afișează mesajul **`NU`**. |

---

##  Restricții

* Se afișează doar **prima pereche** întâlnită.

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `ce face acum el la mare.` | `face acum` |
| `o floare mica si frumoasa.` | `NU` |

---

##  PROBLEMA 3: Cuvinte Prefixe

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Sunt formate din litere mici (`a`–`z`).  
* **Separatorii:** Sunt spațiul (` `) și setul de caractere: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Identificarea cuvintelor care sunt prefixe** | Se afișează, pe rânduri separate, cuvintele care sunt prefixe ale altor cuvinte din text, în **ordinea apariției** în textul original. |

---

##  Restricții

* Un cuvânt **nu** este considerat prefix al lui însuși.  
* Fiecare cuvânt se afișează o singură dată.

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `Inainte de a avea acel ceas, a muncit mult.` | `a` |
| `Eu initial, am avut o initializare in ambele domenii.` | `initial` <br> `am`|

---

##  PROBLEMA 4: Decodare Text

##  Descriere și Reguli

Se citește un text codificat.

* **Cuvintele:** Pot conține litere mari/mici, cifre și simboluri.  
* **Separatorii:** Spațiul (` `) este singurul separator.

---

##  Cerințe Funcționale

| Operație cerută | Regula de decodificare | Ieșire la consolă |
| :--- | :--- | :--- |
| **Filtrare cuvinte** | Dacă un cuvânt **conține cel puțin o cifră**, el este eliminat. Dacă **nu conține nicio cifră**, el este păstrat și afișat. | Cuvintele păstrate, separate printr-un spațiu, în ordinea apariției lor. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `ana are 3mere si 5 pere` | `ana are si pere` |
| `A1b este codat corect` | `este codat corect` |

---

##  PROBLEMA 5: Cuvinte 22

##  Descriere și Reguli

Se citește un text urmat de o literă.

* **Cuvintele:** Sunt formate din litere mici (`a`–`z`).  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.  
* **Litera $C$:** Este o literă mică citită separat.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Filtrare după frecvență** | Se afișează, pe rânduri separate, cuvintele din text care conțin litera $C$ de **exact două ori**. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `a` <br> `ana are mere si banane` | `ana` <br> `banane` |
| `r` <br> `barometru caramida arici` | `barometru` |

---

##  PROBLEMA 6: Cuvinte 1

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`–`z`).  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Filtrare capete egale** | Se afișează, pe rânduri separate, cuvintele care încep și se termină cu aceeași literă. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `ala are multe mere dar nu face un efort minim sa ia si pentru mine unu` | `ala` <br> `unu` <br> `minim` |

---

##  PROBLEMA 7: Poziții

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`–`z`).  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Filtrare după poziție** | Se afișează, pe rânduri separate, cuvintele care se află pe poziții impare (1, 3, 5 etc.) în text. |

---

##  Restricții

* Începe numărarea cuvintelor de la 1 

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `maria are mere si pere` | `maria` <br> `mere` <br> `pere` |

---

##  PROBLEMA 8: Cuvinte 21

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`–`z`).  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.  
* **Vocalele:** `a, e, i, o, u`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Filtrare după număr de vocale** | Se afișează, pe rânduri separate, cuvintele care conțin **cel puțin două vocale**. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `ana are mere si pere` | `ana` <br> `are` <br> `mere` <br> `pere` |

---

##  PROBLEMA 9: Vocale

##  Descriere și Reguli

Se citește un text compus din litere și separatori.

* **Vocalele:** `a, e, i, o, u`.  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Numărare vocale** | Se afișează numărul total de vocale din text. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `mama are mere` | `6` |

---

##  PROBLEMA 10: Cuvinte 2

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`–`z`).  
* **Vocalele:** `a, e, i, o, u`.  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Filtrare consoane pure** | Se afișează, prin spațiu, cuvintele care conțin mai mult de jumătate din lungimea lor **consoane**. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `frate meu a facut un test` | `frate facut test` |

---

##  PROBLEMA 11: Inițiale

##  Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`–`z`).  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Afișare inițiale** | Se afișează, pe un singur rând, inițialele fiecărui cuvânt, separate printr-un spațiu. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `ana are mere si pere` | `a a m s p` |

---

##  PROBLEMA 12: ProSir

##  Descriere și Reguli

Se citește pe o linie un cuvânt $C$, iar pe următoarea linie textul $T$ de prelucrat.

* **Cuvântul $C$:** Cuvântul care trebuie eliminat.  
* **Cuvintele din $T$:** Litere mici (`a`–`z`).  
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Filtrare cuvânt specific** | Se afișează textul rezultat după eliminarea tuturor aparițiilor cuvântului $C$. Spațiile și separatorii trebuie menținuți corect (fără spații duble). |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `cel` <br> `cel mai bun, cel mai frumos.` | `mai bun, mai frumos.` |

---

##  PROBLEMA 13: A1Z26 (Codificare)

##  Descriere și Reguli

Se citește un text care conține litere mari și mici, precum și separatori.

* **Literele:** `A–Z` și `a–z`.  
* **Regula:** Literele se mapează la poziția lor în alfabet (ignorând majusculele/minusculele):  
  $A/a \rightarrow 1, B/b \rightarrow 2, \dots, Z/z \rightarrow 26$.  
* **Separatorii:** Spațiul (` `) și alte caractere sunt ignorate.

---

##  Cerințe Funcționale

| Operație cerută | Ieșire la consolă |
| :--- | :--- |
| **Codificare alfanumerică** | Se afișează textul codificat, unde fiecare literă este înlocuită cu numărul corespunzător poziției sale, iar numerele sunt separate printr-un spațiu. Separatorii sunt ignorați. |

---

##  Exemple

| Intrare | Ieșire |
| :--- | :--- |
| `Ana are mere.` | `1 14 1 1 18 5 13 5 18 5` |
