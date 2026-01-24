#include <stdio.h>
#define N 100
typedef struct Produs
{
    char denumire[30];
    float pretUnitar;
    unsigned int cantitate;
};
struct Produs v[N];
void afisare(struct Produs v[], int lungime)
{
    for(int i=0; i<lungime; i++)
    {
        printf("Produs %d: %s %.2f %d \n", i+1, v[i].denumire, v[i].pretUnitar, v[i].cantitate);
    }
}
void ieftinire(float s, struct Produs v[], int lungime)
{
    for(int i=0; i<lungime; i++)
    {
        float stoc=v[i].pretUnitar*v[i].cantitate;
        if(stoc>s)
        {
            v[i].pretUnitar=v[i].pretUnitar-(v[i].pretUnitar*10)/100;
        }
    }
}
int main()
{
    int n;
    float s;
    printf("n=");
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        printf("Produs #%d:\ndenumire: ", i+1);
        scanf("%s", v[i].denumire);
        printf("Pret unitar: ");
        scanf("%f", &v[i].pretUnitar);
        printf("Cantitate: ");
        scanf("%d", &v[i].cantitate);
    }
    afisare(v, n);
    printf("s=");
    scanf("%f", &s);
    ieftinire(s, v, n);
    afisare(v, n);
    return 0;
}
