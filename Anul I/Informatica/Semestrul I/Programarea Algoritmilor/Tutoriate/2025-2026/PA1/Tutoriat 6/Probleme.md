## 1. NrXDivImp

Folosind metoda **Divide et Impera**, scrieți funcția recursivă cu antetul:

```python
def NrXDivImp(a[], st, dr, x)
```

care primind ca parametri un vector `a` de numere întregi și trei numere întregi `st`, `dr` și `x`, returnează numărul de apariții ale numărului `x` în secvența `a[st], a[st+1], ..., a[dr]`.

###  Restricții și precizări

* `st ≤ dr`
* Numele funcției este **NrXDivImp**.
* Vectorul `a` este indexat de la **1**.

###  Exemplu

Dacă `a = (2, 5, 1, 5, 3, 5, 5, 5, 7, 6)`, atunci:

* `NrXDivImp(a, 1, 6, 5)` returnează **3** (deoarece în secvența `2, 5, 1, 5, 3, 5` numărul `5` apare de `3` ori).
* `NrXDivImp(a, 9, 10, 5)` returnează **0**.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. AlternDivImp

Folosind metoda Divide et Impera, scrieți funcția recursivă cu antetul:

```python
def AlternDivImp(a[], st, dr)
```
care primind ca parametri un vector `a` de numere naturale și două numere întregi `st` și `dr`, returnează `1` dacă în secvența `a[st], a[st+1], ..., a[dr]` numerele impare alternează cu cele pare, sau returnează `0` dacă există cel puțin două numere alăturate de aceeași paritate.

###  Restricții și precizări

* `st ≤ dr`
* Numele funcției este **AlternDivImp**.
* Vectorul `a` este indexat de la **1**.

### Exemplu

Dacă `a = (1,2,3,4,5,6,7,8,9,11)`, atunci :

* `AlternDivImp(a, 1, 10) = 0`, deoarece numerele 9 și 11 aflate pe poziții alăturate au aceeași paritate
* `AlternDivImp(a, 1, 8) = 1`

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 3. QuickSort

Folosind metoda Divide et Impera, scrieți funcția recursivă cu antetul:

```python
def QuickSort(a[], st, dr)

```
care primind ca parametri un vector `a` de numere întregi și două numere întregi `st` și `dr`, ordonează crescător elementele din secvența `a[st], a[st+1], ..., a[dr]` folosind algoritmul QuickSort.

### Restricții și precizări

* `st ≤ dr`
* Numele funcției este **AlternDivImp**.
* Vectorul `a` este indexat de la **1**.
* Se va utiliza metoda de partiționare specifică algoritmului QuickSort.

### Exemplu
input:

```python
12
10 0 -1 -3 1 -4 9 3 -1 -4 3 -4

```

output:

```python
-4 -4 -4 -3 -1 -1 0 1 3 3 9 10

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 4. SumPrimDEI

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`, determinați suma elementelor prime din acest șir.

### Exemplu
input:

```python
6
4 11 8 4 3 5 

```

output:

```python
19

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 5. CntImpare

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`,  determinați câte elemente impare sunt în acest șir.

### Exemplu
input:

```python
6
4 1 8 4 3 5 

```

output:

```python
3

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 6. ExistaPrimeDivImp

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`,  să se verifice dacă în şir există elemente prime.

### Exemplu
input:

```python
5
21 8 6 10 8

```

output:

```python
NU

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 7. SumPareVec

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`, determinați suma elementelor pare din acest șir.

## Restricții și precizări

* `1 ≤ m, n ≤ 100`
* numerele din matrice vor fi mai mici decât `1.000.000`

intput: 

```python
6
4 1 8 4 3 5 

```

output:

```python
16

```

## 8. VerifEgaleDivImp

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`, să se verifice dacă toate elementele vectorului sunt egale.

## Restricții și precizări

* `1 ≤ n ≤ 500`
* fiecare element al vectorului va avea cel mult patru cifre

intput: 

```python
7
6 6 6 6 4 6 6 

```

output:

```python
NU

```

## 9. Maxim6

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`, determinați cel mai mare element din acest șir.

## Restricții și precizări

* `1 ≤ n ≤ 1000`
* numerele din matrice vor fi mai mici decât `1.000.000`

intput: 

```python
6
4 1 8 4 3 5 

```

output:

```python
8

```

## 10. VerifNrParCifreDivImp

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`, să se verifice dacă toate elementele şirului au număr par de cifre.

## Restricții și precizări

* `1 ≤ n ≤ 100`
* elementele şirului sunt numere naturale nenule cu cel mul 9 cifre

intput: 

```python
5
2820 82 65 1026 84

```

output:

```python
DA

```

## 11. Hanoi

Turnurile din Hanoi este un joc matematic sau, dacă vreți, un puzzle. Este format din trei tije `A`, `B` și `C` și un număr variabil de discuri, de diferite diametre. Inițial discurile sunt așezate în ordine descrescătoare a diametrelor pe tija `A`, de la vârf către bază, astfel încât să formeze un turn.
Scopul jocului este acela de a muta toate discurile de pe tija `A` pe tija `C` folosind ca tijă intermediară tija `B`, respectând următoarele reguli:

* la un moment dat doar un singur disc poate fi mutat
* fiecare mutare constă în luarea celui mai de sus disc de pe o tija și mutarea acestuia pe o altă tijă
* un disc cu diametrul mai mare nu poate fi poziționat deasupra unui disc cu diametrul mai mic.


Dacă se cunoaște numărul n de discuri aflate pe tija `A`, să se determine șirul mutărilor necesare pentru ca toate discurile să fie mutate pe tija `C`.

Fișierul de ieșire `hanoi.out` va conține pe prima linie numărul `m`, ce reprezintă numărul minim de mutări ce se efectuează. Pe următoarele `m` linii vor fi scrise mutările sub forma: **tija sursă->tija destinație**.

`hanoi.in`
```python
2

```

`hanoi.out`
```python
3
A->B
A->C
B->C

```








