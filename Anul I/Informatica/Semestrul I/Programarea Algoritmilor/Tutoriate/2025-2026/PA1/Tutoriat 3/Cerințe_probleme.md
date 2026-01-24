# Probleme: List Comprehensions

**List comprehensions** în Python oferă o modalitate concisă și eficientă de a crea liste noi.

---

## Problema 1: Pătratele numerelor

Creează o listă nouă care să conțină pătratele numerelor întregi de la a la b.

**Soluție:**

### Input:
```python
3 5
```

### Output:
```python
[9,16,25]
```

## Problema 2: Numere negative

Creează o listă nouă care să conțină doar numerele negative dintr-o listă dată.

### Input:
```python
[5, -2, 10, -8, 0, -1, 7]
```
### Output:
```python
[-2,-8,-1]
```

## Problema 3: Numere pare

Folosind o listă dată, creează o listă nouă care să conțină doar numerele pare.

### Input:
```python
[1,3,54,65,789,3,4,6]
```

### Output:
```python
[54,4,6]
```

## Problema 4: Cuvinte cu o anumită lungime

Dintr-o propoziție, extrage doar cuvintele care au mai puțin de n litere.
Pe prima linie se va citi propoziția, iar pe linia următoare n. Să se întoarcă lista cuvintelor care respectă cerința și **-1** dacă nu există nici un cuvânt.

### Input:
```python
Îmi place să fiu un programator
3
```

### Output: 
```python
["să","un"]
```

## Problema 5: Conversie litere mari

Convertește toate cuvintele dintr-o listă în majuscule.

### Input:
```python
["mere", "banane", "cirese"]
```

### Output: 
```python
['MERE', 'BANANE', 'CIRESE']
```

## Problema 6: Elevi eminenți

Un fișier text numit `note.txt` care conține pe fiecare linie numele unui student și nota sa (separate prin spațiu). Folosind list comprehension, citește fișierul și creează o listă care să conțină numele studenților care au obținut o notă mai mare sau egală cu 9.

### Input:
`note.txt`
```python
Ion 7
Maria 9
Petru 6
Elena 10
George 8
Ana 9
```

### Output: 
```python
["Maria", "Elena", "Ana"]
```

## Problema 7: Extragere cifre

Se citește o propoziție și se cere formarea unei liste care conține toate cifrele din acea propoziție.

### Input:

```python
Am 2 mere si 5 banane, costa 12 lei.
```

### Output:
```python
[2,5,1,2]
```


## Problema 8

Ai o listă de numere. Creează o listă nouă care să conțină doar rădăcinile pătrate ale numerelor care sunt divizibile cu 4.

### Input:
```python
[4,17,64,99]
```

### Output:
```python
[2.0,8.0]
```

## Problema 9: Orașele

Se dă o listă de orașe. Vrei să creezi o listă nouă care să conțină doar orașele care se află la un index par (0, 2, 4, etc.) în lista originală *și* care au o lungime a numelui mai mare de 5 caractere.

### Input:
```python
orase = ["Bucuresti", "Brasov", "Cluj", "Timisoara", "Sibiu","Chisinau", "Constanta"]
```
### Output: 
```python
['Bucuresti', 'Constanta']
```

# Probleme: List Comprehensions pentru Matrice

## Problema 10: Produsul indicilor

Creează o matrice pătrată $n \times n$ în care fiecare element este produsul indicilor săi ($i \times j$).

### Input:
```python
n = 3
```
### Output:
```python
[[0, 0, 0],
 [0, 1, 2],
 [0, 2, 4]]
```

## Problema 11: Elemente pozitive în matrice

Dintr-o matrice dată, extrage toate elementele strict pozitive într-o listă simplă.

### Input:
```python
1 -2 3
-1 0 2
5 -6 0
```
### Output:
```python
[1, 3, 2, 5]
```

## Problema 12: Suma fiecărei linii

Dintr-o matrice, creează o listă cu suma elementelor fiecărei linii.

### Input:
```python
1 2 3
4 5 6
7 8 9
```
### Output:
```python
[6, 15, 24]
```
## Problema 13: Flatten matrice

Transformă o matrice $n \times m$ într-o listă simplă cu toate elementele ei.

### Input:
```python
1 2
3 4
5 6
```
### Output:
```python
[1, 2, 3, 4, 5, 6]
```

## Problema 14: Elemente pare din matrice

Dintr-o matrice, creează o listă cu toate elementele pare.

### Input:
```python
1 2 3
4 5 6
7 8 9
```
### Output:
```python
[2, 4, 6, 8]
```

## Problema 15: Indici cu valori pozitive

Dintr-o matrice $n \times m$, creează o listă cu perechi $(i, j)$ pentru elementele strict pozitive.

### Input:
```python
0 -1
2 3
```
### Output:
```python
[(1, 0), (1, 1)]
```
## Problema 16: Transpunere matrice

Creează transpunerea unei matrice folosind list comprehension.

### Input:
```python
1 2 3
4 5 6
```
### Output:
```python
[[1, 4], [2, 5], [3, 6]]
```

## Problema 17: Suma pară

Din două liste $a$ și $b$, creează o listă de tupluri $(x, y)$ pentru fiecare pereche de elemente ($x$ din $a$ și $y$ din $b$) dacă $x + y$ este par.

### Input:
```python
a = [1, 2]
b = [3, 4]
```
### Output:
```python
[(1, 3), (2, 4)]
```
## Problema 18: Cuvinte palindrom

Pe prima linie a fisierului `propozitie.in` este o propozitie cu cuvinte separate prin " " si cu `.` la sfarsit , extrage toate cuvintele care sunt palindroame și care au o lungime mai mare de 3 caractere, și afișează lista în `propozitie.out`.

### Input:
`propozitie.in`
```python
Ana are radar civic si level si pop.
```
### Output:
 `propozitie.out`
```python
['radar', 'civic', 'level']
```

## Problema 19: Flatten matrice cu condiție

Dintr-o matrice, creează o listă simplă cu toate elementele care sunt mai mari decât 5.

### Input:
```python
1 6 3
7 4 9
2 8 5
```
### Output:
```python
[6, 7, 9, 8]
```

## Problema 20: Matrice boolean

Dintr-o matrice de numere, creează o matrice boolean unde fiecare element este `True` dacă este pozitiv (strict mai mare decât zero) și `False` altfel.

### Input:
```python
1 -1
0 5
```
### Output:
```python
[[True, False], [False, True]]
```
## Problema 21: Index și valoare (Valori impare)

Dintr-o listă de numere, creează o listă de tupluri $(index, valoare)$ doar pentru valorile impare.

### Input:
```python
lista_data = [2, 3, 4, 5, 6]
```
### Output:
```python
[(1, 3), (3, 5)]

```

## Problema 22: Linie cu suma maximă

Dintr-o matrice, creează o listă cu liniile al căror total depășește un prag $k$.

### Input:
```python
1 2 3
4 5 6
7 8 9
k = 10
```
### Output:
```python
[[4, 5, 6], [7, 8, 9]]
```


