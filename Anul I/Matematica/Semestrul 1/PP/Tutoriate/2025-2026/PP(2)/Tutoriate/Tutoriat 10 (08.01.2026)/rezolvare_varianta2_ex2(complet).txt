#ex 2

#a)
f = open("date2.txt")
ls = [linie.strip().split(", ") for linie in f.readlines()]
f.close()
d = dict()
for lista in ls:
    if lista[1] in d.keys():
        if lista[2] in d[lista[1]].keys():
            produs = [lista[0]]
            produs.extend(lista[3:])
            d[lista[1]][lista[2]].append(produs)
        else:
            produs = [lista[0]]
            produs.extend(lista[3:])
            d[lista[1]][lista[2]] = [produs]
    else:
        produs = [lista[0]]
        produs.extend(lista[3:])
        d[lista[1]] = dict()
        d[lista[1]][lista[2]] = [produs]
print(d)
#%%
#b)

for categorie in d:
    print(categorie)
    for subcategorie in d[categorie]:
        chilipir = min(d[categorie][subcategorie], key = lambda lista: float(lista[2][:len(lista[2]) - 4]) )
        print(subcategorie + ':', " ".join(chilipir), sep = "\t")
    print()
    
#%%
#c)

def creare_fisier(*ls, d):
    for subcategorie in ls:
        f = open("".join([subcategorie, ".txt"]), 'w')
        for categorie in d:
            if subcategorie in d[categorie]:
                for produs in d[categorie][subcategorie]:
                    f.write(" ".join(produs) + "\n")
        f.close()
        
creare_fisier("lactate", "mezeluri", "imbracaminte", d=d)

#%%
#d)

import re

def marca(nume):
    return re.findall('[A-Z][a-z]+', open(nume).read())

print(marca("lactate.txt"))
