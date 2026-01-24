def consoane_comune(*cuvinte):
    d = {}
    vocale = 'aeiouAEIOU'
    l_consoane = []
    for cuvant in cuvinte:
        l_consoane = [litera for litera in cuvant if litera not in vocale]
        lista = sorted(list(set(l_consoane)))
        cheie = ""
        for i in lista:
            cheie+=i
        if cheie not in d:
            d[cheie] = []
        d[cheie].append(cuvant)
    lmax = 0
    rez = []
    for i,j in d.items():
        if len(j) > lmax:
            lmax = len(j)
            rez = j
    print(f'Lungimea maxima este {lmax} iar lista este {rez}')
    return lmax
consoane_comune("este","stea","are","rea","tasta")


lista_numere = [800,246,153,12]
prefix_5 = [x for x in lista_numere if all((x // 10**i) % 5 != 0 for i in range(len(str(x))))]
print(prefix_5)