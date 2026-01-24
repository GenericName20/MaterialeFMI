# 1. Matrice + multimi


def citire_matrice(nume_fisier):
    with open(nume_fisier, "r") as f:
        linii = [line.strip() for line in f if line.strip() != ""]

    mat = []
    for linie in linii:
        mat.append(list(map(int, linie.split())))

    # verificam ca toate liniile au aceeasi lungime
    if not mat:
        return []

    m = len(mat[0])
    for row in mat:
        if len(row) != m:
            return None
    return mat


def _prima_egala_ultima(x):
    s = str(x)
    return s[0] == s[-1]


def multimi(matrice, *indici):
    # multimea de negative: facem intersectie
    inter_neg = None
    # multimea de pozitive cu prima cifra = ultima: facem reuniune
    reun_poz = set()

    for idx in indici:
        linie = matrice[idx]

        neg = {v for v in linie if v < 0}
        poz = {v for v in linie if v > 0 and _prima_egala_ultima(v)}

        if inter_neg is None:
            inter_neg = neg
        else:
            inter_neg = inter_neg.intersection(neg)

        reun_poz |= poz

    if inter_neg is None:
        inter_neg = set()

    return inter_neg, reun_poz


def main():
    mat = citire_matrice("matrice.in")
    if mat is None:
        print("Fisier invalid")
        return

    n = len(mat)

    # ultimele 3 linii: n-3, n-2, n-1
    _, poz_ultimele_3 = multimi(mat, n - 3, n - 2, n - 1)
    print(*sorted(poz_ultimele_3))

    # negative comune primei si ultimei linii
    neg_comun, _ = multimi(mat, 0, n - 1)
    print(len(neg_comun))
