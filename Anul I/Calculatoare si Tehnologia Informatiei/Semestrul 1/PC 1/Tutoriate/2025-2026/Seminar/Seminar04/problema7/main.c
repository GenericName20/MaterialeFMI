#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct participanti{
    char nume[20];
    int nrinscriere;
    float note[3];
    float media;
}v[100];
int n;

void sortalfabetic(){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-1;j++){
            if(strcmp(v[j].nume,v[j+1].nume)>0){
                struct participanti aux;
                aux=v[j];
                v[j]=v[j+1];
                v[j+1]=aux;
            }
        }
    }
}


void sortmedie(){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-1;j++){
            if(v[j].media<v[j+1].media){
                struct participanti aux;
                aux=v[j];
                v[j]=v[j+1];
                v[j+1]=aux;
            }
        }
    }
}


void calculmedie(){
    for(int i=0;i<n;i++){
        float sum=0;
        for(int j=0;j<3;j++){
            sum+=v[i].note[j];
        }
        v[i].media=sum/3;
    }
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("lista_ordonata.txt","w");
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++){
        fscanf(fin,"%s",v[i].nume);
        fscanf(fin,"%d",&v[i].nrinscriere);
        for(int j=0;j<3;j++){
            fscanf(fin,"%f",&v[i].note[j]);
        }
    }
    sortalfabetic();
    calculmedie();
    for(int i=0;i<n;i++){
        fprintf(fout,"%s ",v[i].nume);
        fprintf(fout,"%d\n",v[i].nrinscriere);
        for(int j=0;j<3;j++){
            fprintf(fout,"%f ",v[i].note[j]);
        }
        fprintf(fout,"\n%f\n",v[i].media);
    }
    sortmedie();
    for(int i=0;i<n;i++){
        printf("%s ",v[i].nume);
        printf("%d\n",v[i].nrinscriere);
        for(int j=0;j<3;j++){
            printf("%f ",v[i].note[j]);
        }
        printf("\n%f\n",v[i].media);
    }
    return 0;
}
