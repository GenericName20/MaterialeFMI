#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    char garb;
    int solutii=-1;
    int a,b,c,x1,x2,delta=0;
    scanf("%d%d%d",&a,&b,&c);
    delta = b*b - 4*a*c;
    if(delta>=0){
        x1= (-b+sqrt(delta))/(2*a);
        x2= (-b-sqrt(delta))/(2*a);
        printf("x1=%d,x2=%d",x1,x2);
    }
    else{
        printf("Rezultatele sunt complexe!");
    }
    return 0;
}
