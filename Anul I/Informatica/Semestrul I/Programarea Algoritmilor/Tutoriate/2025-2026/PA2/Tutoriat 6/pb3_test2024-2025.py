import json
from textwrap import indent

f=open("depozite.in")
d={}
cheie_banca=nume_moneda=None
for linie in f:
    linie=linie.strip()
    if "Banca: " in linie:
        sir=linie[7:]
        cheie_banca,parte_moneda=sir.split(',')
        nume_moneda=parte_moneda[9:]
        if cheie_banca not in d:
            d[cheie_banca]={}
        if nume_moneda not in d[cheie_banca]:
            d[cheie_banca][nume_moneda]=[]
    elif linie !="":
        suma,dobanda,perioada=linie.split()
        suma=int(suma)
        dobanda=float(dobanda)
        perioada=int(perioada)
        d[cheie_banca][nume_moneda].append([suma,dobanda,perioada])
print(json.dumps(d,indent=2))

def actualizeaza_depozite(d,*args,m,p,x):
    for banca in d:
        if banca in args:
            if m in d[banca]:
                for dep in d[banca][m]:
                    if dep[2]>=x:
                        dep[1]+=p
    return d

d=actualizeaza_depozite(d,"Banca Transilvania",m="LEI",p=2,x=12)
print(json.dumps(d,indent=2))


f.close()
