#1

#a
# g=open("citire.out", "w") #cere close
# with open("citire.in", "r") as f:
#     x=f.read()
#     g.write(x)

# g.close()
    
#b
# g=open("citire.out", "w") #cere close
# with open("citire.in", "r") as f:
#     while x := f.readline(): # walrus operator
#         g.write(x)

# g.close()

#sau
# g=open("citire.out", "w") #cere close
# with open("citire.in", "r") as f:
#     x = f.readline()
#     while x: # walrus operator
#         g.write(x)
#         x = f.readline()

# g.close()

#c
# g=open("citire.out", "w") #cere close
# with open("citire.in", "r") as f:
#     x = f.readlines()
#     g.writelines(x)

# g.close()

#3
# f=open("matrice.in")

# m,n = f.readline().strip().split()
# m, n=int(m), int(n)
# print(m, n)

# # matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]
# # lrezultat=[max(linie) for linie in matr]

# matr=[max([int(caracter) for caracter in linie.strip().split()]) for linie in f]

# # lrezultat=[int(max(linie)) for linie in f]

# print(matr)

# f.close()

#4
# f=open("matrice.in")

# m,n,k = f.readline().strip().split()
# m, n,k=int(m), int(n), int(k)

# matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]
# matr[k+1:k+1]=[[0]*n]

# print(matr)

# f.close()

#5
# def produs(linie):
#     p=1
#     for elem in linie:
#         p*=elem
#     return p

# f=open("matrice.in")

# m,n = f.readline().strip().split()
# m, n=int(m), int(n)

# matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]

# rez=[produs(linie) for linie in matr].count(max(produs(linie) for linie in matr))

# #lista.count(cautat)

# print(rez)

# f.close()

#6
# f=open("matrice.in")

# m,n,k= f.readline().strip().split()
# m, n, k=int(m), int(n), int(k)
# k=k%n

# matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]

# matr = matr[m-k:]+matr[:m-k]

# print(matr)

# f.close()

#7
# f=open("matrice.in")

# m,n= f.readline().strip().split()
# m, n=int(m), int(n)

# matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]

# matrTransp=[[linie[i] for linie in matr] for i in range(n)]

# matrTransp2 = list(list(t) for t in zip(*matr))

# print(matrTransp)
# print(matrTransp2)

# f.close()

#9
# f=open("matrice.in")

# m,n= f.readline().strip().split()
# m, n=int(m), int(n)

# matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]

# lista=[sum(linie)-max(linie) for linie in matr]

# print(lista)

# f.close()

# 10
# f=open("matrice.in")

# m,n= f.readline().strip().split()
# m, n=int(m), int(n)

# matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]

# for i in range(m):
#     if i%2:
#         print(*matr[i][::-1])
#     else:
#         print(*matr[i])

# f.close()

#16
f=open("matrice.in")

m,n= f.readline().strip().split()
m, n=int(m), int(n)

matr=[[int(caracter) for caracter in linie.strip().split()] for linie in f]

matr90=[[matr[j][i] for j in range(m-1, -1, -1)]for i in range(n)]

print(matr90)

f.close()