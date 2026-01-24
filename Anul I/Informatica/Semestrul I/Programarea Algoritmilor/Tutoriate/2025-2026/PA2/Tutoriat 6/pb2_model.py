from collections import defaultdict
f=input()
d=defaultdict(int)
d = {}
ds=defaultdict(list)
ls=[]
with open (f, 'r') as fin:

    for linie in fin:
        for i in linie.strip().split():
            d[i.lower()]+=1

    for key,value in d.items():
        ds[value].append(key)
    for key in ds:
        ds[key].sort()
    ls=sorted(ds.keys(), key=lambda x: -x)
for i in ls:
    print(f"Frecventa {i}: {', '.join(ds[i])}")





