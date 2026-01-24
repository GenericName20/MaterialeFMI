#ex 2

#a)
f = open("date2.txt")

ls = [linie.strip() for linie in f.readlines()]
f.close()

ls = [linie.split(", ") for linie in ls]
print(ls)
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
    for subcategorie in d[categorie]:
        
        chilipir = min(d[categorie][subcategorie], key = lambda lista: float(lista[2][:len(lista[2]) - 4]) )
        print(chilipir)