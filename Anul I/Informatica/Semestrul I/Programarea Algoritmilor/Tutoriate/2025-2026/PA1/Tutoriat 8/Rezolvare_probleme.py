#1
def produs_maxim():
    n = int(input())

    input_data = [int(input()) for x in range(n)]
    # print(input_data)

    # n = int(input_data[0])
    arr = list(map(int, input_data[1:]))

    arr.sort()

    prod1 = arr[0] * arr[1]
    prod2 = arr[-1] * arr[-2]

    print(max(prod1, prod2))

produs_maxim()


#2
def reparatii_masini():
    line1 = input().split()
    n, t = int(line1[0]), int(line1[1])
    timpi = list(map(int, input().split()))

    timpi.sort()

    count = 0
    timp_consumat = 0

    for durata in timpi:
        if timp_consumat + durata <= t:
            timp_consumat += durata
            count += 1
        else:
            break

    print(count)

reparatii_masini()


#3
def mos_craciun():
    line1 = input().split()
    n, s = int(line1[0]), int(line1[1])
    preturi = list(map(int, input().split()))

    preturi.sort()

    bani_cheltuiti = 0
    cadouri_cumparate = 0

    for pret in preturi:
        if bani_cheltuiti + pret <= s:
            bani_cheltuiti += pret
            cadouri_cumparate += 1
        else:
            bani_ramasi = s - bani_cheltuiti
            necesar = pret - bani_ramasi
            print(f"{cadouri_cumparate} {necesar}")
            return

    print(f"{cadouri_cumparate} 0")

mos_craciun()


#4
def proiecte_investitii():
    n = int(input())
    timpi = list(map(int, input().split()))

    # creăm o listă de tupluri (timp, index_original)
    # indexul e i+1 deoarece problema cere indici de la 1 la n
    proiecte = []
    for i in range(n):
        proiecte.append((timpi[i], i + 1))

    proiecte.sort(key=lambda x: x[0])

    rezultat = [str(x[1]) for x in proiecte]
    print(" ".join(rezultat))

proiecte_investitii()


#5
def eureni():
    line = input().split()
    s, n, e = int(line[0]), int(line[1]), int(line[2])


    # generăm bancnotele descrescător: e^n, e^(n-1), ..., e^0
    bancnote = []
    valoare_curenta = e ** n
    for _ in range(n + 1):
        bancnote.append(valoare_curenta)
        valoare_curenta //= e

    total_bancnote = 0
    rezultat = []

    for b in bancnote:
        if s == 0:
            break
        numar = s // b  # câte bancnote de tipul b intră
        if numar > 0:
            s %= b  # restul rămas de plată
            total_bancnote += numar
            rezultat.append(f"{b} {numar}")

    for r in rezultat:
        print(r)
    print(total_bancnote)

eureni()



#6
A = list(map(int, input("A = ").strip("[]").split(",")))
B = list(map(int, input("B = ").strip("[]").split(",")))

m = len(A)

A_sorted = sorted(A)
B_sorted = sorted(B)

# selectam m elemente din B
neg_count = sum(1 for x in A_sorted if x < 0)
pos_count = m - neg_count

# cele mai mici pentru negative
B_neg = B_sorted[:neg_count]
# cele mai mari pentru pozitive
B_pos = B_sorted[-pos_count:] if pos_count > 0 else []

# construim perechile
pairs = []
suma = 0

for i in range(neg_count):
    prod = A_sorted[i] * B_neg[i]
    suma += prod
    pairs.append((A_sorted[i], B_neg[i]))

for i in range(pos_count):
    a = A_sorted[neg_count + i]
    b = B_pos[i]
    prod = a * b
    suma += prod
    pairs.append((a, b))

print(suma)

exp = " + ".join([f"{x}*{y}" for x, y in pairs])
print(f"Explicație: {suma} = {exp}")



#7
def umplere_bazin():
    galeti = list(map(int, input().split()))
    C = int(input())

    galeti.sort(reverse=True)

    folosite = []

    for g in galeti:
        if g <= C:
            C -= g
            folosite.append(g)

    if C == 0:
        print(*(folosite[::-1]))
    else:
        print("Nu este posibil")

umplere_bazin()



#8
m, n = map(int, input().split())

A = []
for _ in range(m):
    A.append(list(map(float, input().split())))

# Vector pentru pozitii (1-indexate)
pozitii = []

# Pornim de la ultimul rand
last_val = max(A[m - 1])
last_col = A[m - 1].index(last_val)

pozitii.append((m, last_col + 1))
suma = last_val

# Parcurgere de jos in sus
for i in range(m - 2, -1, -1):
    best_val = -1
    best_col = -1

    for j in range(n):
        if A[i][j] < last_val and A[i][j] > best_val:
            best_val = A[i][j]
            best_col = j

    # actualizam
    last_val = best_val
    suma += best_val
    pozitii.append((i + 1, best_col + 1))

pozitii.reverse()

print(f"{suma:.2f}")
for lin, col in pozitii:
    print(lin, col)



#9
N = int(input())
X = list(map(float, input().split()))

X.sort(reverse=True)

K = N + 1  # +1 pentru Nea Vasile
suma = 0.0

for val in X:
    suma += val / K
    K -= 1

if abs(suma - int(suma)) < 1e-9:
    print(int(suma))
else:
    print(f"{suma:.3f}")



#10
A = list(map(int, input().split()))
n = len(A)

# caz trivial
if n == 1:
    print(1)
    exit()

parent = [-1] * n
parent[0] = 0

cur_end = 0
far = 0
best_pos = 0

for i in range(n):
    if i + A[i] > far:
        far = i + A[i]
        best_pos = i

    # cand terminam un "nivel"
    if i == cur_end:
        # setam parintele pentru urmatoarele pozitii
        for j in range(cur_end + 1, min(far + 1, n)):
            if parent[j] == -1:
                parent[j] = best_pos

        cur_end = far
        if cur_end >= n - 1:
            break

# reconstructie traseu
path = []
pos = n - 1
while pos != parent[pos]:
    path.append(pos + 1)
    pos = parent[pos]
path.append(1)

path.reverse()

print(*path)


#11
n = int(input())
g = float(input())

weights = []
for i in range(1, n + 1):
    w = float(input())
    weights.append((w, i))  # (greutate, index)

weights.sort()

pairs = []
i = 0

while i < n - 1:
    w1, idx1 = weights[i]
    w2, idx2 = weights[i + 1]

    if abs(w1 - w2) <= g:
        pairs.append((idx1, idx2))
        i += 2  
    else:
        i += 1

print(len(pairs))
for x, y in pairs:
    print(f"{x} + {y}")

