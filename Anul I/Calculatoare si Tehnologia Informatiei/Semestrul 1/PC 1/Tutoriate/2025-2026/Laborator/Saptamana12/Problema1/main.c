#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void verif(void *a,void *b,int size,int mara,int marb,int *rez){
    *rez=0;
    if(mara!=marb)
        *rez=-1;
    if(mara==marb){
        for(int i=0;i<mara;i++){
            if(memcmp((char*)a + i * size, (char*)b + i * size, size) != 0){
                *rez=-1;
                break;
            }
        }
    }
}

int aint[100],bint[100];
char achar[100],bchar[100];
float afloat[100],bfloat[100];

int main()
{
    FILE * fin = fopen("text.in","r");
    FILE * fout = fopen("text.out","w");
    int n1,m1,n2,m2,n3,m3;
    ///int
    fscanf(fin,"%d%d",&n1,&m1);
    for(int i=0;i<n1;i++)
        fscanf(fin,"%d",&aint[i]);
    for(int i=0;i<m1;i++)
        fscanf(fin,"%d",&bint[i]);
    ///string
    fscanf(fin,"%d%d",&n2,&m2);
    fscanf(fin,"%s",achar);
    fscanf(fin,"%s",bchar);
    ///float
    fscanf(fin,"%d%d",&n3,&m3);
    for(int i=0;i<n3;i++)
        fscanf(fin,"%f",&afloat[i]);
    for(int i=0;i<m3;i++)
        fscanf(fin,"%f",&bfloat[i]);

    int r=0;
    verif(aint,bint,sizeof(int),n1,m1,&r);
    if(r==0)fprintf(fout,"DA!\n");
    else fprintf(fout,"NU!\n");

    verif(achar,bchar,sizeof(char),n2,m2,&r);
    if(r==0)fprintf(fout,"DA!\n");
    else fprintf(fout,"NU!\n");

    verif(afloat,bfloat,sizeof(float),n3,m3,&r);
    if(r==0)fprintf(fout,"DA!\n");
    else fprintf(fout,"NU!\n");
    return 0;
}
