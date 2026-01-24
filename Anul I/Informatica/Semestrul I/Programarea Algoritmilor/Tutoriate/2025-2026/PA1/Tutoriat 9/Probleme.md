# PROBLEMA 1

**Complexitatea maximă a soluției:** `O(n²)`


Pentru două cuvinte `x` și `y`, formate doar din litere mici ale alfabetului englez, spunem că **x este în relație cu y** dacă **ultima literă din x** este **alăturată (consecutivă)** în alfabet cu **prima literă din y**.

Exemple:
- litera `a` este alăturată literei `b`
- litera `b` este alăturată literelor `a` și `c`
- etc.


Se citesc de la tastatură:
- un număr natural `n`
- un șir de `n` cuvinte, formate doar din litere mici ale alfabetului englez

Cuvintele sunt date pe **o singură linie**, separate prin spații.

Să se elimine din șir **un număr minim de cuvinte**, astfel încât șirul rămas să respecte următoarea proprietate:

> Orice cuvânt din șir, cu excepția ultimului, este în relație cu următorul cuvânt din șir.

1. Se vor afișa pe ecran **cuvintele eliminate**.
2. Se va determina dacă **soluția optimă este unică**.
3. Se va afișa un mesaj corespunzător:
   - `solutia este unica`
   - `solutia nu este unica`


## Date de intrare

```text
7
casa apa bun bine fila dop orar

```

## Date de iesire

```text
casa bun fila
solutia nu este unica
```



---


# PROBLEMA 2

**Complexitatea maximă a soluției:** `O(n²)`

Să se determine un **subșir crescător de lungime maximă** al unui șir `t` format din `n` numere întregi.

### Date de intrare

```text
8
10 5 8 3 9 4 12 6

```

### Date de iesire
```text
5 8 9 12

```


---



# PROBLEMA 3 

**Complexitatea maximă a soluției:** `O(n²)`

Martinel a terminat sesiunea de examene și și-a propus ca mâine să se uite cât mai mult la televizor. Pentru aceasta și-a făcut o listă cu `n` emisiuni pe care ar vrea să le vadă.

Pentru fiecare emisiune a notat:
- intervalul de desfășurare **[s, t)** (ora și minutul de început și de sfârșit)
- **numele postului** care difuzează emisiunea (poate conține spații)

Martinel vrea să vadă o emisiune **de la început până la final**, fără întrerupere (deci fără a schimba postul în timpul emisiunii).


Scrieți un program Python care să îl ajute pe Martinel să aleagă o listă de emisiuni la care să se uite mâine astfel încât:

- emisiunile selectate să nu se suprapună (să poată fi urmărite integral)
- **suma duratelor** emisiunilor selectate să fie **maximă**

Programul va afișa:
1. lista emisiunilor selectate (în formatul din exemplu), câte una pe linie
2. dacă soluția optimă este **unică** sau **nu este unică**


## Date de intrare

```text
10 10 10 30 post 1
10 05 11 00 post 2
9 10 10 00 post 1
10 40 12 00 post 3
11 40 12 10 post 2
```

## Date de iesire

```text
[9:10, 10:00) post 1
[10:10, 10:30) post 1
[10:40, 12:00) post 3
solutia este unica
```


---



# PROBLEMA 4

**Complexitatea maximă a soluției:** `O(n²)`


Alice vrea să își schimbe parola la contul de email. Ea are:
- un șir de caractere preferat `s` (format din caractere ASCII) de lungime `n`
- un număr preferat `k`

Alice construiește o parolă **ștergând caractere** din șirul `s`, astfel încât șirul obținut să respecte proprietatea:

> Pentru orice două caractere aflate pe poziții consecutive în parola obținută, diferența dintre codurile lor ASCII (în modul) este **≥ k**.

Alice dorește ca parola să fie **cel mai lung** șir care se poate obține astfel din `s`.


Scrieți un program Python care:
1. citește șirul `s` și numărul `k`
2. determină o parolă de **lungime maximă** ce se poate obține din `s` prin ștergeri, respectând condiția `|ASCII(c1) - ASCII(c2)| ≥ k` pentru caractere consecutive
3. afișează parola găsită
4. determină dacă soluția optimă este **unică** și afișează:
   - `solutia optima este unica` sau
   - `solutia optima nu este unica`



## Date de intrare

```text
iepurasul_si_Alice_@.tara_minunilor
15

```


## Date de iesire

```text
euas_s_Al@.tarau
solutia optima nu este unica

```

---



# PROBLEMA 5

**Complexitatea maximă a soluției:** `O(mn)`


Greiereșul vrea să fie harnic vara aceasta și să adune singur grăunțe pentru iarnă, fără să mai ceară de la furnici.

El se află pe un câmp reprezentat ca o **tabelă dreptunghiulară** cu `m` linii și `n` coloane. În fiecare pătrățel pot exista:
- **grăunțe** (valoare pozitivă sau zero)
- **furnici** (valoare negativă) care îi cer grăunțe

Reguli:
- Când ajunge într-o celulă cu **grăunțe**, le adună.
- Când ajunge într-o celulă cu **furnici** (valoare `cij < 0`), furnicile îi cer `-cij` grăunțe.
  - Greiereșul poate trece prin acea celulă **doar dacă are suficiente grăunțe** ca să le dea.
  - În acest caz, grăunțele lui scad cu `-cij`.

Greiereșul pornește din **colțul din dreapta sus** (celula `(1, n)`) și se poate deplasa doar în celule vecine:
- la **vest** (stânga)
- la **sud** (jos)
- la **sud-vest** (diagonal jos-stânga)

Se poate opri în **orice celulă de pe ultima linie**, unde își construiește adăpostul pentru iarnă.


Scrieți un program Python care:
1. citește dimensiunile tablei `m`, `n` și valorile `cij`
2. determină un traseu valid pentru Greiereș astfel încât să adune un **număr maxim de grăunțe**
3. afișează:
   - numărul maxim de grăunțe obținute pe traseu
   - traseul (lista coordonatelor celulelor parcurse), ca în exemplu



## Date de intrare

```text
4 4
5 2 3 1
-14 7 1 -2
1 -10 -3 15
-1 6 12 2

```

## Date de iesire

```text
maxim 20 graunte pe traseul
1 4
1 3
2 3
3 3
4 3
4 2
```


---



# PROBLEMA 6


Schiorel a urcat cu telecabina până în vârful stațiunii și își dorește să ajungă **cât mai obosit** la una dintre cabanele stațiunii, ca să se poată hidrata cât mai intens.

Stațiunea este reprezentată ca o **matrice pătratică** de dimensiune `n × n`, în care fiecare element poate fi:
- un număr natural `cij` = gradul de oboseală acumulat dacă Schiorel trece prin celula `(i, j)`
- `-1` = în acea celulă se află o **cabană**

Schiorel:
- poate începe traseul din **orice celulă de pe prima linie**
- se poate opri la **orice cabană** (odată ajuns la o cabană, se oprește)
- se poate deplasa doar în jos:
  - **direct în jos**: `(i+1, j)`
  - **diagonal stânga-jos**: `(i+1, j-1)`
  - **diagonal dreapta-jos**: `(i+1, j+1)`
- evident, fără a ieși din matrice


Scrieți un program Python care:
1. citește `n` și matricea `c`
2. determină un traseu care pornește de pe prima linie și se termină într-o celulă cu valoarea `-1` (cabană),
   astfel încât **oboseala totală acumulată să fie maximă**
3. afișează:
   - valoarea maximă a oboselii
   - traseul ales (coordonatele celulelor parcurse), câte una pe linie


## Date de intrare

```text
4
5 2 6 11
-1 7 1 -1
4 10 3 5
1 6 -1 2

```

## Date de iesire

```text
Gradul de oboseala maxim 23
1 3
2 2
3 2
4 3

```





## Date de intrare

```text
4
5 2 6 31
-1 7 -1 -1
4 10 3 5
1 6 -1 2

```

## Date de iesire

```text

Gradul de oboseala maxim 31
1 4
2 3

```

---










