ex = int(input("Introdu numarul exercitiului : "))

if ex == 1 :
    n = int(input())
    numere = []
    for _ in range(n):
        numar = int(input())
        numere.append(numar)
    numere.sort()
    print(max(numere[0]*numere[1], numere[-1]*numere[-2]))

elif ex == 2 :
    nr_masini=int(input())
    timp_total=int(input())
    timp_masina=[]
    for _ in range(nr_masini):
        timp=int(input())
        timp_masina.append(timp)
    timp_masina.sort()
    contor=0
    while(timp_total-timp_masina[contor]>0):
        timp_total -= timp_masina[contor]
        contor+=1
    print(contor)

elif ex == 3:
    with open ("proiecte.in") as f:
        nr_proiecte = f.readline()
        poz_proiect = [x for x in f.readline().split()]
        contor = 1
        # proiect = []
        # for i in poz_proiect:
        #     proiect.append((contor, int(i)))
        #     contor += 1
        proiect = [(i+1,timp) for i,timp in enumerate(poz_proiect)]
        print(proiect)
        proiect.sort(key = lambda t: t[1])
    for i, timp in proiect:
        print(i, end=" ")

elif
