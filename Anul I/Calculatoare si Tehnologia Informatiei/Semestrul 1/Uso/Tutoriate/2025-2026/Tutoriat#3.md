# TUTORIAT SISTEME DE OPERARE #3

## Lucrul cu fisiere


### Librarii

Pentru manipularea fisierelor este necesar sa includeti aceste librarii (sunt folositoare mereu):
```c
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
```
Daca sunteti curiosi, puteti sa cautati ce contine fiecare librarie si pentru ce este folosita.

### Functii (vechi) pentru manipularea fisierelor

O parte din functiile folosite pentru fisiere sunt depasite si nu prea mai sunt folosite decat in scop educational. Cu toate acestea, ele sunt usor de inteles si trebuie sa le cititi pentru primele probleme de la examen (acelea la care vi sa da un cod si se cere ce se afiseaza).

`int open(const char *pathname, int flags [, mode_t mode]);` 
* exact una dintre:
    * `O_RDONLY` = deschidere doar pentru citire;
    * `O_WRONLY` = deschidere doar pentru scriere;
    * `O_RDWR` = deschidere pentru citire _si scriere;
* 0 sau mai multe dintre:
    * `O_TRUNC` = dacă fișierul există, este regular și am specificat O_WRONLY sau O_RDWR, vechiul conținut se șterge;
    * `O_CREAT` = dacă fișierul nu există, se va crea (ca fișier regular vid); în acest caz, trebuie să fie prezent și parametrul 'mode';
    * `O_EXCL` = dacă am folosit O_CREAT și fișierul există, funcția se termină cu eroare; 
    * `O_APPEND` = înainte de fiecare scriere în fișier indicatorul poziției curente se va muta automat la sfârșit;
    * `O_NONBLOCK` = apelul lui 'open()' este neblocant (în cazul când ar trebui să producă adormirea procesului (vezi mai jos), n-o face ci se termină cu eroare);
    * `O_SYNC` = orice scriere în fișier va bloca procesul până când informația ajunge efectiv din bufferul sistemului pe disc;

`int close(int desc);`
* inchide fisierul cu descriptorul __desc__

`int dup(int oldfd);`
* creaza un nou descriptor pentru fisierul __oldfd__
* modificarile de continut si de cursor din __oldfd__ vor aparea in noul descriptor si invers

`int dup2(int oldfd, int newfd);`
* asemanator cu functia `dup`

`off_t lseek(int desc, off_t offset, int origine);`
* `SEEK_SET` (=0) = inceputul fisierului
* `SEEK_CUR` (=1) = pozitia curenta
* `SEEK_END` (=2) = sfarsitul fisierului

`ssize_t read(int desc, void *buf, size_t nr);`

`ssize_t write(int desc, void *buf, size_t nr);`

V-am lasat mai jos o problema care s-a dat acum 2 ani la examen. Se cere ce se afiseaza in urma executiei acestui cod:

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main()
{
        int d1,d2;
        char x,y;
        d1=open("f", O_CREAT| O_TRUNC|O_RDWR, S_IRWXU);
        write(d1,"123456789",9*sizeof(char));
        lseek(d1,0,SEEK_SET);
        if(fork())
        {
                d2=dup(d1);
        }
        else
        {
                d2=open("f",O_RDWR);
                sleep(1);
        }

        read(d2,&x,sizeof(char)); read(d1,&y,sizeof(char));
        printf("%c %c\n",x,y);
        wait(NULL);
}
```


---

### Functii (noi) pentru manipularea fisierelor

Aceste functii sunt ceva mai utilizate deoarece nu folosesc _descriptori de fisiere_, ci folosesc __pointeri la tipul FILE__. O sa dati de aceste functii la cursul de PC1 si la USO, unde o sa le folositi la probleme de laborator si la examen (partea unde trebuie sa scrieti cod).

`FILE* fopen(const char pathname, const char* flags);` 
* functia returneaza un pointer la tipul FILE prin care putem accesa fisierul
* flags pot fi: “r” - read, “w” – write, “a” – append

`int fclose(FILE *stream);`
* functia inchide fisierul

`int fseek(FILE *stream, long int offset, int origin);`
* asemanator la ca `lseek`

`void rewind(FILE *stream);`
* functia muta cursorul din fisier la inceputul fisierului

`long ftell(FILE *stream);`
* aceasta functia returneaza numarul de octeti (sau caractere) de la pozitia cursorului pana la inceputul fisierului
* aceasta functie poate fi folosita pentru a afla cate caractere are un fisier

`int feof(FILE *stream);`
* functia testeaza daca am ajuns la finalul fisierului

Cam orice problema de fisiere se rezolva cu aceaste functii. Cu toate acestea, apar situatii in care folositi functii din libraria `dirent.h` pentru manipularea directoarelor dar vom discuta in cadrul urmatorului tutoriat. 
Mai jos aveti un exemplu de problema ce se foloseste de aceste functii:

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Utilizare: %s fis1 fis2\n", argv[0]);
        return EXIT_FAILURE;
    }

    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        perror(argv[1]);
        return EXIT_FAILURE;
    }

    FILE *g = fopen(argv[2], "r");
    if (g == NULL) {
        perror(argv[2]);
        fclose(f);
        return EXIT_FAILURE;
    }

    fseek(f, 0, SEEK_END);
    int size_f = ftell(f);
    rewind(f);

    fseek(g, 0, SEEK_END);
    int size_g = ftell(g);
    rewind(g);

    if (size_f < size_g) {
        fprintf(stderr, "Sirul din %s este mai scurt decat sirul din %s\n", argv[1], argv[2]);
        fclose(f);
        fclose(g);
        return EXIT_FAILURE;
    }

    int c1 = fgetc(f), c2 = fgetc(g), cnt = 0;
    while (c1!=EOF && c2!=EOF) {
        if (c1 != c2)
        {
            int size_aux=ftell(g);
            rewind(g);
            fseek(f, -size_aux + 1,SEEK_CUR);
        }
        if (ftell(g) == size_g) {
            cnt++;
            rewind(g);
            fseek(f, -size_g + 1, SEEK_CUR);
        }
        c1 = fgetc(f);
        c2 = fgetc(g);
    }

    if (cnt != 0)
        printf("Sirul din %s apare in sirul din %s de %d ori\n", argv[2], argv[1], cnt);
    else
        printf("Sirul din %s nu apare in sirul din %s\n", argv[2], argv[1]);

    fclose(f);
    fclose(g);

    return 0;
}
```
