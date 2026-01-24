#include <stdio.h>

int ispalindrom(int n,int rez){
    if(n==0)
        return rez;
    int primcf,ultcf,newn=0;
    ultcf=n%10;
    if(n<10)
        primcf=n;
    else{
        n/=10;
        while(n>10){
            newn=newn*10+n%10;
            n/=10;
        }
        primcf=n;
    }
    printf("Primcf: %d Ultcf: %d\n",primcf,ultcf);
    if(primcf!=ultcf){
        return ispalindrom(0,0);
    }
    else
        return ispalindrom(newn,rez);
}

int main() {
    int n;
    scanf("%d",&n);
    int rez = ispalindrom(n,1);
    if (rez==0)
        printf("Nu este palindrom\n");
    else
        printf("Este palindrom\n");
    return 0;
}