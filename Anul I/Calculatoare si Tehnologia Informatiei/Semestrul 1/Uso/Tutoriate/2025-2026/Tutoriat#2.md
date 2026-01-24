# TUTORIAT SISTEME DE OPERARE #2

## Environmentul

Environmentul reprezinta totalitatea variabilelor de mediu ce descriu un proces.
Aceste variabile sunt intotdeauna de forma “NAME=VALUE” si au diferinte functionalitati.
Una dintre aceste variabile este `PATH` – daca avem un program executabil in unul din path-urile din aceasta variabila, executabilul respective poate fi executat de oriunde.

## Afisarea environmentului

* Prin al treilea parametru al functiei main – `char** envp`

> !!! Acest parametru ne ajuta sa vizualizam environmentul procesului la inceputul acestuia.
> Daca vrem sa modificam variabilele de mediu, trebuie folosit `environ`.!!!

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv, char** envp)
{
    for(int i=0; envp[i]!=NULL; i++)
        printf("%s\n", envp[i]);

    return 0;
}
```
* Prin utilizarea variabilei externe (vizibila pentru toate procesele din calculator) – `extern char** environ`

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char** environ;

int main(int argc, char** argv, char** envp)
{
    char** env=environ;
    while(*env!=NULL)
    {
      printf("%s\n",*env);
      env++;
    }

    return 0;
}
```
## Funcții C pentru Variabile de Environment

Toate aceste funcții sunt definite în header-ul `<stdlib.h>`.

### `getenv`

```c
#include <stdlib.h>
char *getenv(const char *name);
```
Returneaza adresa de inceput a stringului - valoare a variabilei de environment cu numele ’name’; daca numele nu corespunde nici unei variabile de environment, returneaza NULL.

### `putenv`

```c
#include <stdlib.h>
int putenv(char *string);
```
Stringul ’string’ trebuie sa fie de forma ’name=value’. 
Functia schimba valoarea variabilei de environment ’name’ la ’value’, daca variabila ’name’ exista, sau adauga aceasta variabila cu aceasta valoare, daca nu exista.
Stringul pointat de ’string’ devine parte a environment-ului, deci alterarea sa ulterioara modifica environmentul.
Functia ’putenv()’ returneaza 0 in caz de succes sau nonzero ( ̧si seteaz ̆a ’errno’) in caz de esec.

### `setenv, unsetenv`

```c
#include <stdlib.h>
int setenv(const char *name, const char *value, int overwrite);
int unsetenv(const char *name);
```
Functia ’setenv()’ adauga sau modifica o variabila de environment:
- daca nu exista variabila cu numele ’name’, adauga aceasta variabila, cu numele ’name’;
- daca exista variabila cu numele ’name’  ̧si ’overwrite’ este nonzero, schimba valoarea variabilei in ’value’;
- daca exista variabila cu numele ’name’  ̧si ’overwrite’ este 0, nu schimba valoarea variabilei  ̧si returneaza succes;
Functia ’setenv()’ face copii ale stringurilor indicate de ’name’  ̧si ’value’, ˆın contrast cu ’putenv()’.
Functia ’unsetenv()’ elimina (delete) variabila ’name’ din environment.
Daca ’name’ nu exista in environment, ’unsetenv()’ returneaza succes  ̧si environmentul ramane neschimbat.
Ambele functii ’setenv()’  ̧si ’unsetenv()’ returneaza 0 in caz de succes sau -1 ( ̧si seteaza ’errno’) in caz de esec.


### `clearenv`

```c
#include <stdlib.h>
int clearenv(void);
```
Sterge (clear) environmentul procesului apelant  ̧si seteaza valoarea variabilei ’environ’ (a se vedea mai jos) la NULL.
Ulterior, se pot ad ̆auga noi variabile cu ’putenv()’  ̧si ’setenv()’.
Functia ’clearenv()’ returneaza 0 in caz de succes sau nonzero in caz de esec.


## Exemplu de utilizarea functiilor de manipulare a environmentului

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    const char* var_name = "MY_CUSTOM_VAR";

    char* initial_value = getenv(var_name);
    if (initial_value == NULL) {
        printf("'%s' is not currently set.\n", var_name);
    } else {
        printf("Initial value of '%s': %s\n", var_name, initial_value);
    }

    printf("Setting '%s' to 'hello_world'.\n", var_name);
    if (setenv(var_name, "hello_world", 1) != 0) {
        perror("setenv failed");
        return 1;
    }

    char* new_value = getenv(var_name);
    if (new_value != NULL) {
        printf("New value of '%s': %s\n", var_name, new_value);
    }

    printf("Trying to set '%s' to 'new_value' (with overwrite=0).\n", var_name);
    setenv(var_name, "new_value", 0);

    char* unchanged_value = getenv(var_name);
    printf("Value after non-overwrite attempt: %s\n", unchanged_value);
    printf("(It should still be 'hello_world')\n");

    printf("Unsetting '%s'.\n", var_name);
    if (unsetenv(var_name) != 0) {
        perror("unsetenv failed");
        return 1;
    }

    char* final_value = getenv(var_name);
    if (final_value == NULL) {
        printf("'%s' has been successfully unset.\n", var_name);
    } else {
        printf("ERROR: '%s' was not unset.\n", var_name);
    }

    return 0;
}
```
