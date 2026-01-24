#include <stdio.h>
#include <stdlib.h>
int n;
struct adresa
{
    char localitate[50];
    char nume_str[50];
    int nr_str;
    char bloc[4];
    int ap;
};
struct data
{
    int zi, luna, an;
};
struct persoana
{
    char nume[255];
    struct adresa adr;
    struct data data_n;
} t[20];
void citire()
{
    do
    {
        printf ("\nintroduceti n");
        scanf("%d", &n);
    }
    while(n<2 || n>=20);
    for (int i = 1; i<=n; i++)
    {
        printf("nume: ");
        scanf("%s", t[i].nume);
        getchar();
        printf("\n adresa este:\n localitate: ");
        fgets(t[i].adr.localitate, 50, stdin);
        printf("\nstrada: ");
        fgets(t[i].adr.nume_str, 50, stdin);
        printf("\n nr strada: ");
        scanf(" %d", &t[i].adr.nr_str);
        getchar();
        printf("\n bloc: ");
        fgets(t[i].adr.bloc, 4, stdin);
        printf("\n apartament: ");
        scanf(" %d", &t[i].adr.ap);
        getchar();
        printf("\n data nasterii: ");
        scanf(" %d %d %d", &t[i].data_n.zi, &t[i].data_n.luna, &t[i].data_n.an);
    }
}
void afisare()
{
    for (int i = 1; i<=n; i++)
    {
        printf("%s ", t[i].nume);
        printf(", adresa: localitate %s strada %s nr. %d bloc %s ap. %d", t[i].adr.localitate,
               t[i].adr.nume_str, t[i].adr.nr_str, t[i].adr.bloc, t[i].adr.ap);
        printf(", data nasterii: %d.%d.%d", t[i].data_n.zi, t[i].data_n.luna, t[i].data_n.an);
    }
}
int main()
{
    citire();
    afisare();
    return 0;
}
