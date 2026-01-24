# Tutoriat #7
## Tuburi
### Ce este un tub(pipe)?
Un tub(sau un pipe) este un canal de comunicatie ce faciliteaza transmiterea unor numere, caractere etc intre 2 procese. Mai exact, un proces va scrie diverse informatii in tub, iar celalalt proces va citi informatiile prezente in tub. Pentru a ne folosi de tuburi trebuie sa cream un vector cu 2 elemente si sa aplicam apelul sistem `pipe` asupra lui. De exemplu:
```c
int main()
{
  int p[2];          //declararea capetelor tubului
  if(pipe(p)==-1)    //verificam daca s-a deschis corect tubul
  {
    perror(p);
    return 1;
  }
//restul codului in care folosim tubul
return 0;
}
```
### Mod de functionare
Este important sa intelegem cum vom folosi un pipe. Acesta are 2 capete: in general, p[0] este capatul prin care se citesc informatii, iar p[1] este capatul in care se scriu informatii. Practic, daca am 2 procese: unul tata si unul copil si vreau sa transmit numere din procesul tata in procesul copil, pentru inceput va trebui sa 
declar un tub si in fiecare proces sa inchid capatul pe care nu il folosesc cu  functia `close(int)`. De asemnea, la finalul utilizarii unui capat de pipe, acesta trebuie inchis. De exemplu:
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int p[2];
    if(pipe(p)==-1)
    {
        perror(p);
        return 1;
    }

    pid_t pid=fork();
    
    if(pid==0)
    {
        close(p[0]);        //inchidem capatul de citire din copil pentru ca folosim copilul doar pentru descriere

        char test='t';
        write(p[1],&test,sizeof(char));
        
        close(p[1]);        //inchidem capatul de scriere deoarece nu il mai folosim
    }
    else
    {
        close(p[1]);        //inchidem capatul de scriere din tata pentru ca folosim tatal doar pentru citire

        char rez;
        read(p[0],&rez,sizeof(char));
        printf("Caracterul transmis: %c\n",rez);
        close(p[0]);        //inchidem capatul de citire deoarece nu il mai folosim
        wait(NULL);
    }
    return 0;
}
```
Se observa ca apar functiile de scriere si de citire rudimentare: `read` si `write`.
* `read (int fileDescriptor, char* buffer, size_t sizeof);`
    Aceasta functie este utilizata pentru a citi _sizeof_ bytes de la _fileDescriptor_ si de a-i salva in _buffer_.
* `write (int fileDescriptor, char* buffer, size_t sizeof);`
    Aceasta functie este utilizata pentru a scrie _sizeof_ bytes la _fileDescriptor_ din _buffer_.
