# Tutoriat #4
## Lucrul cu directoare
### Librarii
Pentru manipularea directoarelor vom avea nevoie de 3 librarii principale:
```c
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
```
### Manipularea directoarelor
Pentru a lucra cu directoarele trebuie sa intelegm cum functioneaza acestea. Cel mai simplu este sa le asemanam cu un fisier in care avem siruri de caractere pe fiecare rand.
```
/
└── work_data/
    ├── .
    ├── ..
    ├── personal/
    │   ├── photos/
    │   └── docs/
    └── projects/
        ├── alpha/
        │   └── source/
        └── beta/
```
In schema de mai sus putem observa cu in folderul work_data avem 4 directoare:
* `.` - referinta la folderul curent (este ascuns)
* `..` - referinta la folderul tata (este ascuns)
* `personal`
* `projects`
  
Practic, in cod, fiecare dintre aceste 4 foldere va fi reprezentata printr-un struct numit `dirent` (directory entry). Scopul acestui struct este de a oferi detalii despre tipul intrarii din director citite. Structura acestui struct este:
```c
struct dirent 
{ 	ino_t d_ino; /* Inode number */ 
    off_t d_off; /* Not an offset */
 	  unsigned short d_reclen; /* Length of this record */  
 	  unsigned char d_type; /* Type of file; not supported by all filesystem types */
  	char d_name[256]; /* Null-terminated filename */ 
 };
```
Pentru a extrage informatii despre directory entry-ul pe care ne aflam putem folosi functia:
```c
int stat(const char* path, struct stat* statbuf);
```
Aici, structul statbuf trebuie declarat inainte de apelul functiei, iar dupa apelul functiei va retine informatii despre ce se afla la intrarea data de paramentru `path`. Structul `stat` arata in felul urmator:
```c
struct stat{
  dev_t st_dev; /* ID-ul dispozitivului ce contine fisierul */
  ino_t st_ino; /* numarul de inod */
  mode_t st_mode; /* protectia */
  unlink_t st_nlink; /* numarul de legaturi fizice (hard links) */
  uid_t st_uid; /* UID al utilizatorului proprietar */
  gid_t st_gid; /* GID al grupului proprietar */
  dev_t st_rdev; /* ID-ul despozitivului, daca este un fisier special, care reprezinta un dispozitiv */
  off_t st_size; /* dimensiunea totala a fisierului, in bytes */
  blksize_t st_blksize; /* dimensiunea "preferata" a blocului pentru I/O eficiente ale sistemului de fisiere (scrierea intr-un fisier in bucati mai mici poate cauza read-modify-rewrite ineficient */
  blkcnt_t st_blocks; /* numarul de blocuri de 512B alocate fisierului (poate fi mai mic decat 'st_size'/512 atunci cand fisierul are goluri) */
  time_t st_atime; /* momentul (time) ultimului acces */
  time_t st_mtime; /* momentul (time) ultimei modificari */
  time_t st_ctime; /* momentul (time) ultimei schimbari a caracteristicilor (last status change) */
};
```
Singurul camp care trebuie tinut in vedere este `st_mode`. Cu ajutorul lui ne putem da seama daca intrarea este un fisier regulat, director etc sau ce drepturi are ownerul, grupul sau altii.
Macrouri pentru tip:
```
S_ISREG(.) => este fisier obisnuit (regular file) ?
S_ISDIR(.) => este director (directory) ?
S_ISBLK(.) => este fisier special bloc (block device) ?
S_ISCHR(.) => este fisier special caracter (character device) ?
S_ISFIFO(.) => este tub (FIFO, named pipe) ?
S_ISSOCK(.) => este socket ?
S_ISLNK(.) => este legatura simbolica (symbolic link) ?
```

Macrouri pentru drepturi:
```
S_IRWXU 	00700 masca pentru drepturile proprietarului
S_IRUSR 	00400 dreptul de citire pentru proprietar (owner)
S_IWUSR 	00200 dreptul de scriere pentru proprietar (owner)
S_IXUSR 	00100 dreptul de executie pentru proprietar (owner)
S_IRWXG 	00070 masca pentru drepturile grupului
S_IRGRP 	00040 dreptul de citire pentru grup (group)
S_IWGRP 	00020 dreptul de scriere pentru grup (group)
S_IXGRP 	00010 dreptul de executie pentru grup (group)
S_IRWXO 	00007 masca pentru drepturile altora
S_IROTH 	00004 dreptul de citire pentru altii (others)
S_IWOTH 	00002 dreptul de scriere pentru altii (others)
S_IXOTH 	00001 dreptul de executie pentru altii (others)
```

## Functii pentru directoare:

* `DIR *opendir(const char *name);`
Deschide directorul name pentru citire, alocă o structură DIR în spațiul de memorie al programului utilizator, o inițializează cu informații despre director, poziționează indicatorul pe prima intrare, și returnează adresa structurii; în caz de eroare, returnează NULL și setează errno.

* `int closedir(DIR *dirp);`
Închide directorul gestionat de dirp, (și descriptorul de fișier asociat) și dezalocă structura DIR pointată de acesta.
Returnează 0 în caz de succes sau -1 (și setează errno) în caz de eșec.
Așadar, structurile DIR nu trebuie alocate cu malloc() sau eliberate cu free(), ele sunt alocate la opendir() și eliberate la closedir().

* `struct dirent *readdir(DIR *dirp);`
Furnizează intrarea curentă din directorul indicat de 'dirp' într-o structură internă, avansează indicatorul la următoarea intrare, și returnează adresa structurii.
Dacă indicatorul era la sfârșitul directorului, returnează NULL iar 'errno' nu este modificat.

* `long telldir(DIR *dirp);`
Returnează poziția curentă a indicatorului structurii 'DIR' indicate de 'dirp'.
În caz de eroare, returnează -1 și setează 'errno'.

* `void seekdir(DIR *dirp, long loc);`
Mută indicatorul structurii 'DIR' indicate de 'dirp' la poziția 'loc'. Următorul apel 'readdir()' va furniza intrarea de la această poziție. Argumentul 'loc' ar trebui să fie o valoare returnată de 'telldir()'.

* `void rewinddir(DIR *dirp);`
Mută (re)poziționează indicatorul structurii 'DIR' indicate de 'dirp' la prima intrare. Astfel, directorul poate fi reparcurs cu 'readdir()' de la început.

* `int mkdir(const char *pathname, mode_t mode);`
Creează directorul specificat de pathname cu drepturile mode.
Drepturile cu care va fi creat în realitate directorul vor fi mode & ~umask & 0777.
Returnează 0 în caz de succes sau -1 (și setează errno) în caz de eșec.

* `int rmdir(const char *pathname);`
Șterge directorul pathname; trebuie să fie gol.
Nu necesită vreun drept pe director, necesită drept de scriere pe directorul părinte, unde se află numele specificat - legătura fizică.
Directoarele, însă, nu pot avea mai multe asemenea nume.
Returnează 0 în caz de succes sau -1 (și setează errno) în caz de eșec.



