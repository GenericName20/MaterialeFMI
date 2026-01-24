import math

# ----------------------------
# Problema 1: Pătratele numerelor
# ----------------------------
a, b = 3, 5
patrate = [x**2 for x in range(a, b+1)]
print("Problema 1:", patrate)

# ----------------------------
# Problema 2: Numere negative
# ----------------------------
lst_neg = [5, -2, 10, -8, 0, -1, 7]
negative = [x for x in lst_neg if x < 0]
print("Problema 2:", negative)

# ----------------------------
# Problema 3: Numere pare
# ----------------------------
lst = [1,3,54,65,789,3,4,6]
pare = [x for x in lst if x % 2 == 0]
print("Problema 3:", pare)

# ----------------------------
# Problema 4: Cuvinte cu o anumită lungime
# ----------------------------
propozitie = "Îmi place să fiu un programator"
n = 3
cuv_scurte = [cuv for cuv in propozitie.split() if len(cuv) < n] or [-1]
print("Problema 4:", cuv_scurte)

# ----------------------------
# Problema 5: Conversie litere mari
# ----------------------------
cuvinte = ["mere", "banane", "cirese"]
majuscule = [cuv.upper() for cuv in cuvinte]
print("Problema 5:", majuscule)

# ----------------------------
# Problema 6: Elevi eminenți
# ----------------------------
with open("note.txt") as f:
    elevi_eminenti = [linie.split()[0] for linie in f if int(linie.split()[1]) >= 9]
print("Problema 6:", elevi_eminenti)

# ----------------------------
# Problema 7: Extragere cifre
# ----------------------------
propozitie = "Am 2 mere si 5 banane, costa 12 lei."
cifre = [int(c) for c in propozitie if c.isdigit()]
print("Problema 7:", cifre)

# ----------------------------
# Problema 8: Rădăcini pătrate divizibile cu 4
# ----------------------------
lst_num = [4,17,64,99]
radical = [math.sqrt(x) for x in lst_num if x % 4 == 0]
print("Problema 8:", radical)

# ----------------------------
# Problema 9: Orașele
# ----------------------------
orase = ["Bucuresti", "Brasov", "Cluj", "Timisoara", "Sibiu","Chisinau", "Constanta"]
orase_filtrate = [oras for i, oras in enumerate(orase) if i % 2 == 0 and len(oras) > 5]
print("Problema 9:", orase_filtrate)

# ----------------------------
# Problema 10: Produsul indicilor
# ----------------------------
n = 3
matrice_prod = [[i*j for j in range(n)] for i in range(n)]
print("Problema 10:", matrice_prod)

# ----------------------------
# Problema 11: Elemente pozitive în matrice
# ----------------------------
matrice = [
    [1, -2, 3],
    [-1, 0, 2],
    [5, -6, 0]
]
pozitive = [x for row in matrice for x in row if x > 0]
print("Problema 11:", pozitive)

# ----------------------------
# Problema 12: Suma fiecărei linii
# ----------------------------
matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sume_linii = [sum(row) for row in matrice]
print("Problema 12:", sume_linii)

# ----------------------------
# Problema 13: Flatten matrice
# ----------------------------
matrice = [
    [1,2],
    [3,4],
    [5,6]
]
flatten = [x for row in matrice for x in row]
print("Problema 13:", flatten)

# ----------------------------
# Problema 14: Elemente pare din matrice
# ----------------------------
matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
pare_matrice = [x for row in matrice for x in row if x % 2 == 0]
print("Problema 14:", pare_matrice)

# ----------------------------
# Problema 15: Indici cu valori pozitive
# ----------------------------
matrice = [
    [0, -1],
    [2, 3]
]
indici_poz = [(i,j) for i,row in enumerate(matrice) for j,x in enumerate(row) if x > 0]
print("Problema 15:", indici_poz)

# ----------------------------
# Problema 16: Transpunere matrice
# ----------------------------
matrice = [
    [1,2,3],
    [4,5,6]
]
transpusa = [[row[i] for row in matrice] for i in range(len(matrice[0]))]
print("Problema 16:", transpusa)

# ----------------------------
# Problema 17: Suma pară
# ----------------------------
a = [1,2]
b = [3,4]
suma_para = [(x,y) for x in a for y in b if (x+y)%2==0]
print("Problema 17:", suma_para)

# ----------------------------
# Problema 18: Cuvinte palindrom din fișier
# ----------------------------
with open("propozitie.in") as f:
    text = f.readline().strip().replace(".", "")
palindroame = [cuv for cuv in text.split() if cuv == cuv[::-1] and len(cuv) > 3]
with open("propozitie.out", "w") as f:
    f.write(str(palindroame))
print("Problema 18:", palindroame)

# ----------------------------
# Problema 19: Flatten matrice cu condiție (>5)
# ----------------------------
matrice = [
    [1,6,3],
    [7,4,9],
    [2,8,5]
]
flatten_cond = [x for row in matrice for x in row if x > 5]
print("Problema 19:", flatten_cond)

# ----------------------------
# Problema 20: Matrice boolean
# ----------------------------
matrice = [
    [1,-1],
    [0,5]
]
matrice_bool = [[x>0 for x in row] for row in matrice]
print("Problema 20:", matrice_bool)

# ----------------------------
# Problema 21: Index și valoare (valori impare)
# ----------------------------
lista_data = [2,3,4,5,6]
ind_val_imp = [(i,x) for i,x in enumerate(lista_data) if x % 2 != 0]
print("Problema 21:", ind_val_imp)

# ----------------------------
# Problema 22: Linie cu suma maximă
# ----------------------------
matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
k = 10
linii_max = [row for row in matrice if sum(row) > k]
print("Problema 22:", linii_max)
