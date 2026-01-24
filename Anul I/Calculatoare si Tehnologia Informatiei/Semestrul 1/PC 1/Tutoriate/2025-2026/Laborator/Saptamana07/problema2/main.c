#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float radical(float a){
    return sqrt(a);
}

float invers(float a){
    return pow(a,-1);
}

float sinus(float a){
    return sin(a);
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    float x;
    scanf("%f",&x);

    float (*pointer[3])(float);
    pointer[0]=radical;
    pointer[1]=invers;
    pointer[2]=sinus;
    
    printf("%f %f %f %f",x,pointer[0](x),pointer[1](x),pointer[2](x));
    return 0;
}
