# Tutoriat #6
## Semnale
### Ce este un semnal? 
Un semnal poate fi vizualizat ca un strop de informatie care are ca scop atentionarea unor procese sau vizeaza modificarea starii proceselor. Orice proces poate sa comunice cu alt proces prin semnale daca
cunoastem pid-ul procesului care vrem sa primeasca semnalul.
### Ce semnale putem folosi
Exista 2 tipuri de semnale: semnale principale (codificate prin numere intregi de la 1 la 31) si semnale runtime (asa scrie pe net; probabil au mai multe denumiri; codificate prin nr intregi de la 32 la 64). 
Principalele semnale "principale" sunt:
  * SIGHUP = 1
  Dacă un terminal întrerupe conexiunea (hangup) procesul lider al sesiunii asociate terminalului primește SIGHUP; când liderul de sesiune se termină, toate procesele aflate în grupul din forground al sesiunii primesc SIGHUP.
  Handler implicit: terminarea.
  * SIGINT=2, SIGQUIT= 3
  Când tastăm de la un terminal Ctrl-c, respectiv Ctrl-\ (de fapt caracterele logice 'intr' și 'quit'), primul, respectiv al doilea semnal este trimis către toate procesele aflate în foreground la terminalul respectiv.
  Handler implicit: terminarea (în cazul lui SIGQUIT se face și un fișier 'core' cu imaginea memoriei).

  * SIGKILL=9
  Este neblocabil și nu îi putem asocia alt handler decât cel implicit.
  Handler implicit: terminarea.
  Acest semnal este folosit de regulă pentru a termina explicit un proces dat.

 * SIGTERM = 15
  Handler implicit: terminarea.
  Este o alternativă la SIGKILL care poate fi blocat și i se poate schimba handlerul; cu SIGKILL forțăm terminarea unui proces, cu SIGTERM doar îi semnalăm că ar trebui să se termine. Este trimis implicit de comanda shell 'kill'.

 * SIGUSR1 = 10,  SIGUSR2 = 12
  Handler implicit: terminarea.
  Nu sunt folosite de sistem, sunt lăsate la dispoziția programatorilor.
  * SIGILL = 4 (instrucțiune ilegală)
  * SIGBUS = 7 (acces incorect la memorie, de ex. acces la adrese nealiniate)
  * SIGFPE = 8 (floating point exception)
  * SIGSEGV = 11 (acces la memorie în afara spațiului de adrese alocate sau care încalcă permisiuni)
  Handler implicit: terminarea și fișier 'core'.
  * SIGPIPE = 13
  Scriere într-un fișier tub fără cititori (a se vedea secțiunea 'Tuburi').
  Handler implicit: terminarea.
  * SIGALRM = 14
  * SIGVTALRM = 26
  * SIGPROF = 27
  Handler implicit: terminarea.
  Sunt folosite de program pentru a-și planifica (folosind 'setitimer()', 'alarm()') un comportament anume după un anumit interval de timp, indiferent de momentul unde se află cu execuția (cu ajutorul unui handler utilizator asociat semnalului).

  * SIGCHLD=17
  Handler implicit: ignorare
  Cand un proces se termină, părintele său primește un semnal SIGCHLD.

  * SIGSTOP 19, SIGCONT = 18
  Semnale folosite la suspendarea / reluarea explicită a unor procese (mecanisme de job control).
  Handler implicit: suspendare, respectiv reluare.
  SIGSTOP nu poate fi blocat și nu i se poate asocia alt handler decât cel implicit.

  * SIGTSTP=20
  Handler implicit: suspendare.
  Este asemănător cu SIGSTOP, dar poate fi blocat și i se poate schimba handlerul.
  Când tastăm de la un terminal Ctrl-z (de fapt caracterul logic 'susp'), semnalul este trimis către toate procesele aflate în foreground la terminalul respectiv ("terminal stop").
  SIGTTIN=21, SIGTTOU =22
  Este primit de procesele aflate în background la un terminal, atunci când încearcă să citească, respectiv. scrie, pe el.
  Handler implicit: suspendare.
  Toate semnalele de mai sus, în afară de SIGKILL și SIGSTOP, pot fi blocate și
  li se poate schimba handlerul. Dacă lui SIGCONT îi instalăm un handler utilizator, efectul de trezire din suspendare se va păstra dar, în plus, după trezire, se va executa handlerul.

### Cum transmitem si cum primit un semnal?
Pentru a utiliza toata sintaxa pentru semnale vom include libraria `signal.h`.\
Pentru a transmite intr-un semnal de la un proces P1 la un proces P2 folosim avem nevoie de 2 componente principale: 
  1) un handler
  2) apelul functiei `kill(pid_t PID_P2, int SIGNAL)`\
Un handler este o functie care stie cum sa modifice comportamentul procesului la primirea unui semnal. O functie handler este de obicei o functie `void` care poate afisa un mesaj sau poate contoriza un numar.\
Exemplu de handler:
```c
void handler(int signal)
{
    printf("Am primit un semnal!\n");
}
```
Odata ce declaram functia handler, mai trebuie sa ii spunem procesului ca functia scrisa de noi vrem sa primeasca semnalele si sa decida cum continua programul. Pentru asta, trebuie sa intram in procesul care
vrem sa primeasca un semnal si sa folosim functia `signal(SEMNAL, NUME_HANDLER);`. De acum, procesul actual stie ca daca primeste un semnal cu numele SEMNAL se va uita la handlerul cu numele NUME_HANDLER.\
In momentul acesta, mai trebuie ca procesul nostru sa primeasca semnale. Pentru asta, vom merge in alt proces si folosi functia `kill(pid_t PID_P2, int SIGNAL)`.\
Exemplu de cod:
```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

void handler(int signal){printf("Am primit un semnal SIGUSR1\n");}

int main()
{
    signal(SIGUSR1, handler);
    

    pid_t pid_copil = fork();
    

    if(pid_copil==0)
    {
        sleep(2);
        pid_t pid_tata = getppid();
        for(int i=0;i<=2;i++)
        {
            kill(pid_tata, SIGUSR1);
            sleep(1);
        }
    }
    else
    {
        wait(NULL);
    }
    return 0;
}
```
Observatii: functia `getppid()` returneaza pid-ul tatalui (daca ne aflam intr-un copil);

### Sigaction

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>
#include <setjmp.h>
#include <sys/wait.h>

int d[2],k;
jmp_buf env;
void h(int n)
{
    ++k;
    write(d[1],&k,sizeof(int));
    siglongjmp(env,k);
}

int main()
{
    struct sigaction sa;
    sa.sa_handler=h;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags=0;
    for(k=NSIG-1;k;--k)
        sigaction(k,&sa,NULL);
    pipe(d);

    if(!sigsetjmp(env,k) && !fork() && !sigsetjmp(env,k) &&!fork())
    {
        close(d[1]);
        read(d[0],&k,sizeof(int));
    }
    else
    {
        close(d[0]);
        ++k;
        write(d[1],&k,sizeof(int));
    }

    while(wait(NULL)!=-1);
    printf("%d\n",k);
    return 0;
}
```
### Masca de semnale
```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <bits/types/sigset_t.h>
#include <asm-generic/signal-defs.h>

void handler1(int sig)
{
    printf("Procesul a primit un semnal de tip SIGUSR1\n");
}

void handler2(int sig){}

int main()
{
    signal(SIGUSR1, handler1);
    signal(SIGUSR2, handler2);
    
    sigset_t mascaSemnale;                    //declaram masca de semnale
    sigemptyset(&mascaSemnale);                //golim masca de semnale din motive sanitare(memorie)
    sigaddset(&mascaSemnale, SIGUSR1);
    sigaddset(&mascaSemnale, SIGUSR2);
    sigprocmask(SIG_SETMASK,&mascaSemnale,0);

    sigemptyset(&mascaSemnale);

    pid_t pid = fork();
    
    if(pid==0)
    {
        //sigprocmask(SIG_SETMASK,&mascaSemnale,0);
        pid_t pid_tata = getppid();
        for(int i=0;i<=9;i++)
        {
            if(i%2==1)
            {
                kill(pid_tata,SIGUSR1);
                sigsuspend(&mascaSemnale); 
            }
        }
    }
    else ///suntem in tata
    {
        for(int k=0;k<5;k++)
        {
            sigsuspend(&mascaSemnale);
            kill(pid,SIGUSR2);
        }
            
        wait(NULL);
    }

    return 0;

}
```
