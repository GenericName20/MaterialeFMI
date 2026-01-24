
ex = int(input("Alegeti exercitiul: "))
if ex == 1 :
    text = input().lower()
    text = text.replace('.'," ")
    d = {}
    cuvinte = [x for x in text.split() if x.isalpha()]
    d = {cuv: cuvinte.count(cuv) for cuv in set(cuvinte)}
    # print(d)
    for i in d.items():
        print(i)
elif ex == 2 :
    studenti={}

    def adauga_student(nume,nota,studenti):
        if nume in studenti:
            print(f"Studentul {nume} exista deja")
        else:
            studenti[nume]=nota
            print(f"Am adaugat studentul {nume}")

    def actualizare_nota(nume,noua_nota,studenti):
        if nume not in studenti:
            print(f"Studentul {nume} nu exista")
        else:
            studenti[nume]=noua_nota
            print(f"Am modificat nota studentului {nume}")

    def medie(studenti):
        suma=sum(studenti.values())
        nr=len(studenti)

        return suma/nr

    adauga_student('Ana', 7,studenti)
    adauga_student('Victor',8,studenti)
    adauga_student('Iulia', 10,studenti)
    actualizare_nota('Iulia', 9,studenti)
    print(f"Media tuturor notelor este {medie(studenti)}")

elif ex == 3 :
    text = input("Introdu textul ").strip()
    cuvinte = text.split()
    d = {}
    for cuv in cuvinte :
        if cuv not in d:
            d[cuv] = {}
            #d[teste] = {}
        for j in set(cuv) : #t,e,s
            if j not in d[cuv] :
                d[cuv][j] = 0
            d[cuv][j]+=cuv.count(j)

    for i in d.items():
        print(i)
elif ex == 4:
    nums = [50, 21, 13, 84, 50, 60]
    dict={}
    for x in nums:
        dict[x]=tuple([d for d in range(2,x) if x%d==0])
    for (i,j) in dict.items():
        print(f'{i}:{j}')

elif ex == 5 :
    set = eval(input("Introdu setul: "))
    tuplu = eval(input("Introdu tuplul :"))

    d = {}

    for nr in set :
        ok = True
        for lista in tuplu :
            if nr in lista :
                ok = False
                if nr not in d:
                    d[nr] = []
                d[nr].append((tuplu.index(lista), lista.count(nr)))
        if (ok) :
            d[nr] = []


    for i in d.items():
        print(i)
elif ex == 6:
    nums = eval(input("Introduceti lista "))
    d={}
    for x in nums:
        avg=sum([int(cif) for cif in str(x)])/len(str(x))
        if avg not in d:
            d[avg]=[]
        d[avg]+=[x]

    for avg in d.keys():
        d[avg]=sorted(d[avg],reverse=True)

    print(d)
elif ex == 7:
    nums = [1011, 234, 8158558, 234]
    d={}
    for x in set(nums):
        if x not in d:
            d[x]=[]
        cif=set(str(x))
        for c in cif:
            d[x]+=[(int(c),str(x).count(c))]

    for (i,j) in d.items():
        print(f"{i}:{j}")
elif ex==8:
    d={}
    sir=input("Introduceti un sir: ").split()
    v="aeiouAEIOU"
    for cuvant in sir:
        if cuvant==cuvant[::-1]:
            vocale=[l for l in cuvant if l in v]
            consoane=[l for l in cuvant if l not in v]

            if len(vocale)>=len(consoane):
                d[cuvant]=list(set(vocale))
            else:
                d[cuvant]=list(set(consoane))

    print(d)

elif ex == 9 :
    with open("text.in") as f :
        text = ""
        text = (" ".join([l.strip() for l in f.readlines()])).lower()

    l_totala = len([x for x in text if x.isalpha()])
    d = {}
    for lit in set(text) :
        if lit.isalpha():
            d[lit] = f"{text.count(lit)/l_totala:.3f}"

    for i in d.items():
        print(i)
elif ex==10:
    with open("numere.in", "r") as f:
        linii=f.readlines()
    subliste=[]
    #eliminare element minim din fiecare lista
    for linie in linii:
        numere=list(map(int, linie.split()))
        minim=min(numere)
        filtrata=[x for x in numere if x!=minim]
        subliste.append(filtrata)

    #determinam lungimea minima
    min_lungime=min([len(l) for l in subliste])

    rezultat=[l[:min_lungime] for l in subliste]

    with open("numere.out", "w") as g:
        for l in rezultat:
            g.write(" ".join(map(str,l))+"\n")









