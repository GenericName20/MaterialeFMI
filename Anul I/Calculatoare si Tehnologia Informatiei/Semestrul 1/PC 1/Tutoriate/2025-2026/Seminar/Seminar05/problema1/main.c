#include <stdio.h>
#include <stdlib.h>

int n;
int *v;

void funcA(int n,int *v){
    for(int i=0;i<n;i++){
        if(*(v+i)>0)
            *(v+i)=0;
    }
}


void funcB(){
    for(int i=0;i<n;i++){
        if(v[i]<0){
            int j=i;
            for(j;j<n-1;j++){
                v[j]=v[j+1];
            }
            n--;
            int *aux = (int *) realloc(v, sizeof(int) * n);
            if (aux != NULL) {
                v = aux;
            }
            i--;
        }
    }
}

double funcC(int n,int *v){
    double med=0,nr=0;
    for(int i=0;i<n;i++){
        if(*(v+i)>0){
            nr+=1;
            med+=*(v+i);
        }
    }
    if(nr!=0)
        return med/nr;
    else return -1;
}

int funcD(int n,int *v,int val){
    for(int i=0;i<n;i++){
        if(*(v+i)==val)
            return i;
    }
    return -1;
}

void funcE(int n,int *v){
    int maxim=0;
    for(int i=0;i<n;i++){
        if(*(v+i)>maxim)
            maxim=*(v+i);
    }
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    fscanf(fin,"%d",&n);
    v = (int*) malloc(n * sizeof(int));
    for(int i=0;i<n;i++){
        fscanf(fin,"%d ",v+i);
    }
    funcB();
    for(int i=0;i<n;i++){
        fprintf(fout,"%d ",*(v+i));
    }
    printf("%d", v[4]);
    return 0;
}
