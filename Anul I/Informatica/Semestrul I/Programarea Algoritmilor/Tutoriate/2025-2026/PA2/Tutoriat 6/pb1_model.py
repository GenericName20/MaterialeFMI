# Să se șteargă de pe iecare linie câte 2 elemente astfel încât suma elementelor din
# matricea rămasă să ie minimă. Să se scrie matricea obținută în ișierul matrice.out (pe
# iecare linie din ișier se vor scrie elementele unei linii din matrice separate prin câte un
# spațiu).

f=open("matrice.in")
mat=[]
for linie in f:
    numere=linie.strip().split()
    for i in range(len(numere)):
        numere[i]=int(numere[i])
    max1=max(numere)
    numere.remove(max1)
    max2 = max(numere)
    numere.remove(max2)
    mat.append(numere)
g=open("matrice.out","w")
for linie in mat:
    for element in linie:
        g.write(f"{element} ")
    g.write("\n")
f.close()
g.close()