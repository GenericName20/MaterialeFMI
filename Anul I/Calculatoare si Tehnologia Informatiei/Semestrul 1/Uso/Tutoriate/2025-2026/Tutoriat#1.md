# TUTORIAT SISTEME DE OPERARE #1

## Topics:

### Instalarea WSL (pentru cei care nu au masina virtuala sau dual boot cu linux) 

1.  Pentru a instala **WSL (Windows Subsystem for Linux)** trebuie sa va descarcati pentru inceput **Ubuntu** din Microsoft Store.
2.  Dupa aceea, deschideti terminalul **Windows PowerShell** si rulati comanda `wsl.exe –install`.
3.  Dupa finalizarea descarcarii, va trebui sa dati restart la laptop/pc[cite: 6]. Cand se deschide sistemul, intrati pe **Ubuntu**.
4.  Se vor instala mai multe lucruri si vi se va cere sa introduceti un **username** si o **parola**. **NU UITATI PAROLA!!!**.
5.  Odata ce se finalizeaza instalarea, va trebui sa instalati un compilator pentru C. Cel mai uzual este **gcc**.
6.  Pentru a-l instala trebuie sa rulati comanda `sudo apt install gcc`. Sistemul va cere parola pe care ati setat-o mai devreme deoarece orice comanda care este precedata de argumentul `sudo` este o comanda data cu drepturi de administrator.
7.  Vor aparea niste erori, asa ca va trebui sa rulati comanda `sudo apt-get update`.
8.  La final reincercati comanda pentru instalarea gcc-ului.

---

## Comenzi uzuale

Exista un set de comenzi uzuale pe care le veti folosi:

* `cd [director/path_catre_un_director]` – mergem in directorul ales
* `cd ..` – merge in directorul parinte (practic facem un pas inapoi)
* `ls` – afiseaza continutul directorului curent
* `mkdir [nume_director]` – cream un director cu numele specificat
* `rmdir [nume_director]` – stergem directorul cu numele specificat (pentru directoare goale)
* `rm -r [nume_director]` – stergem un director care contine lucruri. `-r` specifica ca va avea loc o stergere recursiva, in care toate elementele incluse in directorul specificat vor fi eliminate.
* `rm [nume_fisier]` – stergem fisierul ales
* **!!!nano este un editor de texte; putem utiliza `nano [nume_fisier]` pentru a deschide un fisier existent sau pentru a crea si deschide un fisier nou!!!** 

---

## Cum lucrez?

1.  In primul rand trebuie creat un fisier cu codul sursa.
2.  Vom utiliza comanda `nano [nume_fisier].c` pentru a face un fisier nou (nu uitati ca trebuie sa aiba terminatia `.c`).
3.  In el vom scrie codul, iar pentru salvare folosim **ctrl x -> y -> enter**.
4.  Odata ce avem un fisier cu cod, il vom compila cu `gcc -Wall -o [nume_executabil] [nume_fisier].c` si vom rula executabilul cu `./[nume_executabil]`.
5.  Puteti stabili orice nume pentru executabil, nu trebuie sa aiba legatura cu numele fisierului care contine codul sursa.

---

## Notiuni elementare in limbajul de programare C

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE* f=fopen("fisier.txt", "r");

    if(f==NULL)
    {
        printf("Eroare la deschiderea fisierului de intrare!");
        return 1;
    }

    int n,x,i,s=0;
    fscanf(f,"%d",&n);

    for(i=1;i<=n;i++)
    {
        fscanf(f, "%d", &x);
        s=s+x;
    }
    fclose(f);

    FILE* g=fopen("fisier.out", "w");
    if(g==NULL)
    {
        printf("Eroare la deschiderea fisierului de intrare!");
        return 2;
    }
    fprintf(g, "Suma este %d\n", s);
    fclose(g);

    return 0;
}
```
## Parametrii Funcției `main`

Funcția principală `main` poate fi definită pentru a accesa datele transmise programului la momentul executării sale, prin intermediul a trei parametri comuni:

| Parametru | Tip | Nume Oficial | Descriere |
| :--- | :--- | :--- | :--- |
| **`int argc`** | `int` | **Argument Count** | Reprezintă **numărul de argumente** primite. Valoarea minimă este **1** (datorită executabilului în sine, ex: `./executabil`). |
| **`char** argv`** | `char**` | **Argument Vector** | O **matrice de șiruri de caractere** unde fiecare element (`argv[0]` până la `argv[argc-1]`) reprezintă un argument furnizat. |
| **`char** envp`** | `char**` | **Environment Pointer** | O **matrice de șiruri de caractere** care conține variabilele de mediu (environment) ale sistemului, în formatul `NUME=VALOARE`. |

---

##  Exercițiu

Să se scrie un program în C care:
1.  Primește exact **10 numere** ca argumente din linia de comandă.
2.  Calculează **media aritmetică** a acestor numere.
3.  Afișează rezultatul într-un **fișier de ieșire** (e.g., `rezultat.txt`) creat în directorul curent.

### ⌨️ Exemplu de Rulare

Presupunând că executabilul se numește `media_calc`:

```bash
# Rulare corectă
./media_calc 10 20 30 40 50 60 70 80 90 100

# Rezultatul (55.00) va fi scris în 'rezultat.txt'
```
# Hint! 
Puteți folosi funcția [atoi()](https://www.geeksforgeeks.org/c/c-atoi-function/) pentru a realiza conversia din tipul string în tipul int.


