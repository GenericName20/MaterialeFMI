# Tutoriat #5
## Procese
### Ce este un proces?
Cel mai simplu putem defini procesul ca o aplicatie care se afla in executie. Mai in contextul cursului _Utilizarii sistemelor de operare_ orice program in C pe care il scriem sau oricare comanda data
in terminal este un proces. Pentru a vedea procesele intr-un anumit moment, putem folosi comanda `ps`. Putem sa mai adaugam diferite optiuni (pentru informatii suplimantare folositi comanda `man ps`).

### Vizualizarea proceselor in C
Primul lucru pe care il luam in vedere este faptul ca orice program scris de noi in C se transforma intr-un proces cand este executat. In acest proces, intructiunile vor fi cele scris de noi in program si se
vor executa de sus in jos (de la declararea functiei main la return-ul final). Acesta va fi `procesul tata`.\
In procesul tata vor exista variabile. Daca noi vrem sa cream un nou proces care sa mosteneasca variabilele din procesul tata vom utiliza functia `pid_t fork()`. In acest moment va aparea un `proces copil`.\
<img style="float: right;" width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/442242b4-c65d-41ff-8031-e1c5592d076a"/>\
Pentru a diferentia actiunile pe care vrem sa le facem intr-un anumit proces, trebuie sa ne uitam la valoarea returnata de functia fork. Aceasta valoare returnata va fi un numar nenul in procesul tata si va 
fi egala cu 0 in procesul copil. Pentru a intelege mai bine, am scris un exemplu mai jos:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    pid_t pidProcesCopil = fork();

    if(pidProcesCopil==0) //pidProcesCopil = 0 => suntem in copil
    {
        printf("Copilul si-a inceput executia!\n");
        sleep(2);
        printf("Copilul si-a terminat executia!\n");
        return 0;         // daca in procesul copil folosim `return` => copilul se va termina
    }

    if(pidProcesCopil!=0)   // => suntem in tata
    {
        printf("Tatal si-a inceput executia!\n");
        wait(NULL);
        printf("Tatal si-a terminat executia!\n");
    }

    return 0;
}
```
Puteti testa pe calculatorul vostru ce afiseaza codul. O __observatie__ importanta este faptul ca programul de mai jos afiseaza prima oara mesajul tatalui si apoi cel al copilului. Acest lucru nu este o regula.
Teoretic ei ar trebui sa ruleze in acelasi timp, dar este imposibil ca 2 procese sa afiseze pe acelasi output un mesaj. Cu toate acestea, la final programul afiseaza mesajul copilului si apoi pe cel al parintelui.
De ce? Comanda `wait(NULL)` este cheia. Putem manipula modul in care procesul tata asteapta terminarea procesului copil cu ajutorul functiilor `wait()` si `waitpid()`.

## Cum putem astepta procesele?

Cum am spus si mai sus, exista 2 functii principale: wait si waitpid. Acestea au rolul de a bloca procesul parinte pana cand copilul a terminat ce avea de facut sau pana cand primeste un semnal de oprire. 
* `pid_t wait(int *wstatus)`
  Aceasta functie asteapta oricare dintre procesele copil sa se termine. Prin parametrul wstatus se vor returna informatii despre terminarea procesului copil. Daca nu ne intereseaza ce returneaza sau ce s-a
  intamplat cu procesul copil folosim `wait(NULL)`, iar daca vrei sa aflam ce s-a intamplat cu procesul copil trebuie sa folosim niste macro-uri:
  * __WUNTRACED__ returnează și dacă copilul a fost stopat (nu doar terminat)
  * __WCONTINUED__ returnează ̧si dacă copilul era stopat și a fost trezit cu un semnal SIGCONT Dacă ’wstatus’ nu este NULL, funcția stochează în zona de tip ’int’ pointată informații despre starea copilului respectiv
  * __WIFEXITED()__ returnează true dacă copilul s-a terminat normal (i.e. ’exit()’, ’_exit()’, sau return din ’main()’)
  * __WEXITSTATUS()__ returnează codul de retur (exit status) al copilului; acesta constă din cei mai puțin semnificativi 8 biți ai valorii date ca argument lui ’exit()’, ’_exit()’, sau returnată din ’main()’; acest macro este util doar dacă ’WIFEXITED()’ a returnat true
  * __WIFSIGNALED()__ returnează true dacă copilul a fost terminat de un semnal
  * __WTERMSIG()__ returnează numărul semnalului care a terminat copilul; acest macro este util doar dacă ’WIFSIGNALED()’ a returnat true
  * __WCOREDUMP()__ returnează true dacă copilul a produs un core dump (un fișier pe disc conținând imaginea memoriei procesului copil la momentul terminării); de exemplu, dacă copilul a primit un semnal SIGQUIT  ̧si l-a tratat cu handler-ul implicit, el s-a terminat  ̧si a produs un core dump; acest macro este util doar dacă ’WIFSIGNALED()’ a returnat true; obs: acest macro nu este specificat în POSIX, nu este disponibil în unele implementări Unix,  ̧si de aceea utilizarea lui trebuie inclusă între #ifdef WCOREDUMP ... #endif
  * __WIFSTOPPED()__ returnează true dacă copilul a fost stopat de un semnal; este util doar dacă s-a folosit WUNTRACED
  * __WSTOPSIG()__ returnează numărul semnalului care a stopat copilul; acest macro este util doar dacă ’WIFSTOPPED()’ a returnat true
  * __WIFCONTINUED(wstatus)__ returnează true dacă copilul a fost trezit de semnalul SIGCONT
* `pid_t waitpid(pid_t pid, int *wstatus, int options)`
  Aceasta functie este asemanatoare cu functia wait, numai ca putem specifica pid-ul copilului pe care il asteptam. De asemenea, in campul `options` putem avea urmatoarele valori:
  * WNOHANG returnează imediat, chiar dacă copilul nu și-a schimbat starea (nu așteaptă)
  * WUNTRACED returnează ̧si dacă copilul a fost stopat (nu doar terminat)
  * WCONTINUED returnează  ̧si dacă copilul era stopat și a fost trezit cu un semnal SIGCONT

Exemple pentru utilizarea functiei wait():
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    pid_t pidProcesCopil = fork();
    int stat;  // variabila in care se va stoca statusul de terminare al procesului copil

    if(pidProcesCopil==0) //pidProcesCopil = 0 => suntem in copil
    {
        sleep(2);
        return 2;
    }

    if(pidProcesCopil!=0)   // => suntem in tata
    {
        wait(&stat);
        if(WIFEXITED(stat))
            printf("%d\n",WEXITSTATUS(stat));
    }


    return 0;
}
```

Exemplu pentru utilizarea functiei waitpid():
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    pid_t pidProcesCopil = fork();
    int stat;  // variabila in care se va stoca statusul de terminare al procesului copil

    if(pidProcesCopil==0) //pidProcesCopil = 0 => suntem in copil
    {
        sleep(2);
        return 2;
    }

    if(pidProcesCopil!=0)   // => suntem in tata
    {
        waitpid(pidProcesCopil, &stat,0);
        if(WIFEXITED(stat))
            printf("%d\n",WEXITSTATUS(stat));
    }


    return 0;
}
```
Observam ca daca punem valoarea 0 la parametrul `options` waitpid asteapta pana cand procesul copil se termina.
