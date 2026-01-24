# 2. Siruri + liste

def modifica_prefix(x, y, prop):
    cuvinte = prop.split()
    modificate = 0

    for i in range(len(cuvinte)):
        if cuvinte[i].startswith(x):
            cuvinte[i] = y + cuvinte[i][len(x):]
            modificate += 1

    return " ".join(cuvinte), modificate


def poz_max(lista):
    mx = max(lista)
    return [i + 1 for i, val in enumerate(lista) if val == mx]


def main():
    a, b = input().split()

    counts = []
    linii_modificate = []

    with open("propozitii.in", "r") as fin:
        for linie in fin:
            linie = linie.rstrip("\n")
            prop_noua, cnt = modifica_prefix(a, b, linie)
            linii_modificate.append(prop_noua)
            counts.append(cnt)

    with open("propozitii_modificate.out", "w") as fout:
        for linie in linii_modificate:
            fout.write(linie + "\n")

    # afisam indicii propozitiilor cu cele mai multe modificari
    indici = poz_max(counts)
    print(*indici)



