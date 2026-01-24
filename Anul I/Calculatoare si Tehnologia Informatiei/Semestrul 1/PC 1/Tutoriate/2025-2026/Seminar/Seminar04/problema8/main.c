#include <stdio.h>
#include <stdlib.h>

int v[128];

int cifracontrol(int nr){
    int suma=0;
    while(nr!=0){
        suma+=nr%10;
        nr/=10;
    }
    return suma;
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++){
        fscanf(fin,"%d",&v[i]);
    }
    int rez=0;
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++){
            int sumper=0;
            for(int h=i;h<j;h++){
                sumper+=v[h];
            }
            if(cifracontrol(sumper)==9)
            {
                for(int h=i;h<j;h++){
                    fprintf(fout,"%d ",v[h]);
                }
                fprintf(fout,"suma:%d \n",sumper);
                rez++;
            }
        }
    }
    fprintf(fout,"%d",rez);
    return 0;
}
