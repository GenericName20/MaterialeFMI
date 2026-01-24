# Tutoriat #8
## Jump-uri
### De ce avem nevoie de asa ceva?
Este foarte simplu! Imaginati-va ca aveti un joc cu mai multe checkpoint-uri. Daca muriti sau ramaneti fara un obiect, puteti sa va intoarceti la ultimul checkpoint. La fel sunt si jump-urile.
### Care este sintaxa?
In primul rand, libraria pe care o folosim este __setjmp.h__. In al doilea rand, trebuie sa luam in considerare 2 functii importante:
* int setjmp(jmp_buf env);
  
  Functia _setjmp_ ne ajuta sa setam *checkpointurile*.
  
* void longjmp(jmp_buf env, int val);

  Functia _longjmp_ ne ajuta sa sarim la checkpointurile anterioare.

Tot la acest pas este necesar sa definim o variabila tip _jmp_buf_ care va stoca state-ul procesorului in momentul executiei. Daca vrem sa avem mai multe checkpointuri in acelasi timp, trebuie declarate mai multe variabile.
Exemplu:
```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf jump_buffer;

void perform_division(int numerator, int denominator) {
    printf("Attempting to divide %d by %d...\n", numerator, denominator);

    if (denominator == 0) {
        printf("Error: Division by zero detected! Jumping back...\n");
        longjmp(jump_buffer, 1);
    }

    printf("Result: %d\n", numerator / denominator);
}

void deep_nested_function() {
    perform_division(10, 2);
    perform_division(10, 0);
    perform_division(10, 5);
}

int main() {

    int jump_val = setjmp(jump_buffer);

    if (jump_val == 0) {
        printf("--- Start of Normal Flow ---\n");
        deep_nested_function();
    } 
    else {
        printf("\n--- Exception Caught! ---\n");
        printf("Recovered from error code: %d\n", jump_val);
    }

    printf("Program continues execution normally.\n");
    return 0;
}
```


### Sigsetjmp (o varianta mai complexa)
Principalul dezavantaj al jump-urilor simple este faptul ca mastile de semnale nu sunt pastrate. Daca vrem sa revenim la mastile de semnale precedente, trebuie sa folosim alte 2 functii, similare cu cele discutate mai devreme.
* int sigsetjmp(sigjmp_buf env, int savesigs);
  
  Functia _sigsetjmp_ ne ajuta sa setam *checkpointurile*; in plus putem salva masca de semnale: daca _savesigs_=0, masca nu se pastreaza si daca _savesigs_!=0 masca se pastreaza
  
* void siglongjmp(sigjmp_buf env, int val);

  Functia _siglongjmp_ ne ajuta sa sarim la checkpointurile anterioare si sa restabilim masca de semnale.

  Exemplu:
```c
#include <stdio.h>
#include <setjmp.h>
#include <signal.h> 
#include <sys/types.h>

sigjmp_buf stare;
void h(int n)
{
    siglongjmp(stare, 1);
}
int main() 
{
    int n, *p = NULL; 
    signal(SIGSEGV, h); 

    int jmpstatus = sigsetjmp(stare,1);

    if (jmpstatus==0) 
        n = *p;

    else fprintf(stderr, "Eroare.\n");  //jmpstatus!=0

return 0;
}
```
  
