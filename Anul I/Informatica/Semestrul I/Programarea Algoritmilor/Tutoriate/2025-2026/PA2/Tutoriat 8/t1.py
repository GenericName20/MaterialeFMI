# A=[3,-2,5,-1,4]
# B=[7,8,-5,2,-4,-1,5]
#
#
#
#
# A.sort()
# B.sort()
# a1=0
# a2=len(A)-1
# b1=0
# b2=len(B)-1
# s=0
#
# while a1<=a2:
#     if A[a1]*B[b1]>A[a2]*B[b2]:
#         s+=A[a1]*B[b1]
#         a1+=1
#         b1+=1
#     else:
#         s+=A[a2]*B[b2]
#         a2-=1
#         b2-=1
# print(s)

inp = ["casa", "apa", "bun", "bine", "fila", "dop", "orar"]
dp = {}

def backtrack(i, lista_curenta):
    if i == len(inp):
        return lista_curenta.copy()

    if (i, lista_curenta[-1]) in dp:
        return dp[(i, lista_curenta[-1])]

    if not lista_curenta or (
        ord(lista_curenta[-1][-1]) + 1 == ord(inp[i][0])
        or ord(lista_curenta[-1][-1]) - 1 == ord(inp[i][0])
    ):
        noua_lista = lista_curenta.copy()
        noua_lista.append(inp[i])
        adaugat = backtrack(i + 1, noua_lista.copy())
        neadaugat = backtrack(i + 1, lista_curenta.copy())

        if len(adaugat) > len(neadaugat):
            dp[(i, noua_lista[-1])] = adaugat.copy()
            return adaugat.copy()
        else:
            dp[(i, lista_curenta[-1])] = neadaugat.copy()
            return neadaugat.copy()

    aux = backtrack(i + 1, lista_curenta.copy()).copy()
    dp[(i, lista_curenta[-1])] = aux.copy()
    return aux

res1 = backtrack(0, [])
res2 = []
for cuvant in inp:
    if cuvant not in res1:
        res2.append(cuvant)
print(res2)



