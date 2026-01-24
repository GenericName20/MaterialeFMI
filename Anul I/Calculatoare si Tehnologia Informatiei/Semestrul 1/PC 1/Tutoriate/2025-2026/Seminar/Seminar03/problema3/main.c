#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int n;
struct dreptunghi
{
    struct punct
    {
        float x,y;
    } A,C;
    float Arie;
} t[21];
void citire ()
{
    scanf ("%d", &n);
    for (int i=1; i<=n; ++i)
    {
        printf ("Coordonatele punctului A sunt:\n");
        scanf ("%f %f", &t[i].A.x, &t[i].A.y);
        printf ("Coordonatele punctului C sunt:\n");
        scanf ("%f %f", &t[i].C.x, &t[i].C.y);
        t[i].Arie=abs((t[i].C.x-t[i].A.x)*(t[i].C.y-t[i].A.y));
    }
}
void sortare ()
{
    for (int i=1; i<n; ++i)
    {
        for (int j=i+1; j<=n; ++j) if (t[i].Arie>t[j].Arie)
            {
                struct dreptunghi aux;
                aux=t[i];
                t[i]=t[j];
                t[j]=aux;
            }
    }
}
void afisare ()
{
    for (int i=1; i<=n; ++i)
    {
        printf ("(%.2f %.2f), (%.2f %.2f); Arie: %.2f ", t[i].A.x,t[i].A.y,t[i].C.x,t[i].C.y,t[i].Arie);
        printf ("\n");
    }
}
int main()
{
    citire ();
    afisare ();
    if(t[1].A.x<=t[2].A.x)
        printf("da");
    else printf("nu");
//sortare ();
//afisare ();
    return 0;
}
