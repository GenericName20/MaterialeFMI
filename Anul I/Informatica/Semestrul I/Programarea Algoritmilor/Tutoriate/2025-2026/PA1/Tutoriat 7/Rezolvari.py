# 1
with open("autori.in") as f:
    autori={}
    def sterge_carte(d,cod_carte):
        for autor,carte in d.items():
            if cod_carte in carte:
                del d[autor][cod_carte]
                return f"Cartea a fost scrisa de {autori[autor][0]} {autori[autor][1]}"
        return "Cartea nu exista"
    def carti_autor(d,cod_autor):
        L=[]
        L.append(autori[cod_autor][0]+' '+autori[cod_autor][1])
        for _,informatii in d[cod_autor].items():
            L.append((informatii[2],informatii[0],informatii[1]))
        return L
    d={}
    m,n=[int(aux) for aux in f.readline().split()]
    for _ in range(m):
        cod_autor,nume,prenume=[aux for aux in f.readline().strip().split()]
        d[cod_autor]={}
        autori[cod_autor]=[nume,prenume]
    for _ in range(n):
        cod_autor,cod_carte,an_aparitie,nr_pagini,titlu=[aux for aux in f.readline().strip().split(maxsplit=4)]
        d[cod_autor][cod_carte]=[an_aparitie,nr_pagini,titlu]
    # print(d)
    # fct=sterge_carte(d,"111")
    # if fct != "Cartea nu exista":
    #     print(fct)
    #     print(d)
    L=carti_autor(d,"11")
    for linie in L:
        print(linie)






# 2
# v1

with open("input.txt") as f:
    d={}
    for line in f:
        p1,p2,culoare, eticheta=line.split(maxsplit=3)
        p1=tuple(int(x) for x in p1.strip("[]").split(","))
        p2=tuple(int(x) for x in p2.strip("[]").split(","))
        info_leg=culoare, eticheta.strip()
        if p1 not in d:
            d[p1]={}
        d[p1][p2]=info_leg
print(d)

#b)

def insereaza_legatura(d,t1,t2,culoare,eticheta):
    if t1 in d and t2 in d[t1]:
        return False
    info=culoare, eticheta
    if t1 not in d:
        d[t1]={}
    d[t1][t2]=info

    return True

if insereaza_legatura(d,(1,2), (1,3), "albastru", "legatura 2")==True:
    print(d)
else:
    print("legatura deja exista")



# v2
# a) Citire
f = open("legaturi.in")
lista = [] #
for linie in f:
    linie = linie.strip()
    parti = linie.split('] [')
    
    p1_str = parti[0].replace('[', '')
    rest = parti[1].split(']')
    p2_str = rest[0]
    
    detalii = rest[1].strip().split(' ', 1)
    
    x1, y1 = p1_str.split(',')
    p1 = (int(x1), int(y1))
    
    x2, y2 = p2_str.split(',')
    p2 = (int(x2), int(y2))
    
    d = {
        'p1': p1,
        'p2': p2,
        'culoare': detalii[0],
        'eticheta': detalii[1]
    }
    lista.append(d)
f.close()

# b) Inserare legatura
def insereaza_legatura(lista, p1, p2, culoare, eticheta):
    gasit = 0
    for elem in lista:
        if (elem['p1'] == p1 and elem['p2'] == p2) or 
           (elem['p1'] == p2 and elem['p2'] == p1):
            gasit = 1
            break
            
    if gasit == 0:
        d_nou = {'p1': p1, 'p2': p2, 'culoare': culoare, 'eticheta': eticheta}
        lista.append(d_nou)
        return True
    return False

# Testare b
print(insereaza_legatura(lista, (1,3), (2,7), "negru", "legatura noua"))
# print(lista) 

# c) Vecini comuni
def vecini(lista, *puncte):
    toate_pct = set()
    for elem in lista:
        toate_pct.add(elem['p1'])
        toate_pct.add(elem['p2'])
        
    sol = []
    for candidat in toate_pct:
        e_vecin_cu_toti = 1
        
        for p_target in puncte:
            legatura_exista = 0
            for elem in lista:
                s = {elem['p1'], elem['p2']}
                if candidat in s and p_target in s and candidat != p_target:
                    legatura_exista = 1
                    break
            if legatura_exista == 0:
                e_vecin_cu_toti = 0
                break
        
        if e_vecin_cu_toti == 1:
            sol.append(candidat)
            
    sol.sort(key=lambda p: p[1], reverse=True)
    return sol

# Testare c
print(vecini(lista, (2,7), (1,2)))




# 3
# a) Citire
f = open("catalog.in")
linii = f.readlines()
f.close()

d = {}
n = int(linii[0].strip())
idx = 1

for i in range(n):
    rand = linii[idx].strip().rsplit(' ', 1)
    nume = rand[0]
    nr_materii = int(rand[1])
    idx += 1

    d[nume] = {}

    for j in range(nr_materii):
        parti = linii[idx].strip().split(',')
        materie = parti[0]
        note = [int(x) for x in parti[1:]]
        d[nume][materie] = note
        idx += 1


# print(d)

# b) Detalii elev
def detalii_elev(d, nume):
    if nume not in d:
        return []

    sol = []
    materii_elev = d[nume]

    for materie in materii_elev:
        note = materii_elev[materie]

        if 0 in note:
            medie = 0
        else:
            s = sum(note)
            m = s / len(note)
            if m < 5:
                medie = 0
            else:
                medie = m

        sol.append((materie, medie))

    # Sortare lexicografica dupa materie
    sol.sort(key=lambda t: t[0])
    return sol


# Testare b
nume_citit = "Ana Maria Pop"  
rez = detalii_elev(d, nume_citit)
print(rez)


# c) Clasament
def clasament(d, *nume_elevi):
    sol = []
    for nume in nume_elevi:
        if nume in d:
            situatie = detalii_elev(d, nume)
            suma_medii = 0
            corigent = 0

            for materie, medie in situatie:
                if medie == 0:
                    corigent = 1
                suma_medii += medie

            if corigent == 1:
                media_gen = 0
            else:
                media_gen = suma_medii / len(situatie)

            sol.append((nume, media_gen))

    # Sortare descrescatoare dupa medie
    sol.sort(key=lambda t: t[1], reverse=True)
    return sol


# Testare c
print(clasament(d, "Ana Maria Pop", "Mihai Popescu"))





#4
#a)
f=open("cinema.txt")
d={}
for linie in f:
    numecinema,film,ore=linie.strip().split(' % ')
    ore=[x for x in ore.split()]
    if numecinema not in d:
        d[numecinema]={}
        d[numecinema][film]=ore
    else:
        d[numecinema][film]=ore
print(d)
f.close()

#b)
def sterge_ore(d,cinema,film,ore):
    for ora in ore:
        if ora in d[cinema][film]:
            d[cinema][film].remove(ora)
    return d[cinema]

#c=input("cinema=")
#f=input("film=")
#o=input("ore=")
print(sterge_ore(d,'Cinema 1', 'Minionii 2',{'12:30','12:00'}))
print(d)

#c
def cinema_film (d,*numecinema,ora_minima,ora_maxima):
    sol=[]
    for cinema in numecinema:
        for film in d[cinema]:
            ok=1
            for o in d[cinema][film]:
                if ora_minima>o or ora_maxima<o:
                    ok=0
            if ok==1:
                tuplu=(film,cinema,d[cinema][film])
                sol.append(tuplu)
    sol.sort(key=lambda t:(t[0],-len(t[2])))
    return sol

print(cinema_film (d,'Cinema 1','Cinema 2',ora_minima="14:00",ora_maxima="22:00"))





