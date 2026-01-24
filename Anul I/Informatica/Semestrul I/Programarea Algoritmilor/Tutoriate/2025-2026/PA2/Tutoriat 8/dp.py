inp=["casa","apa","bun","bine","fila","dop","orar"]
v=[1]*len(inp)
p=[-1]*len(inp)

def ver(c1,c2):
    if ord(c1[-1])-1==ord(c2[0]) or ord(c1[-1])+1==ord(c2[0]):
        return True
    return False

for i in range(1,len(inp)):
    for j in range(i-1,-1,-1):
        if ver(inp[j],inp[i]):
            if 1+v[j]>v[i]:
                v[i]=1+v[j]
                p[i]=j

pmax=v.index(max(v))
res=[]
while pmax!=-1:
    res.append(inp[pmax])
    pmax=p[pmax]

for j in inp:
    if j not in res:
        print(j,end=" ")

