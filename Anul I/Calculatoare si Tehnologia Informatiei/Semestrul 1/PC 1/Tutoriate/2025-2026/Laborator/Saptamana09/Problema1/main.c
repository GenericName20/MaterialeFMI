#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n,m;

char *inserez(char *p, char *s,int poz){
    int done=0;
    p = realloc(p,n*m*sizeof(char));
    for(int i=poz;i<=poz+m;i++){
        for(int j=poz;j<n+m;j++){
            p[poz+1]=p[poz];
        }
        p[poz]=s[done];
        done++;
    }
}

char *sterg(char *p, int poz, int cate){
    int done=0;
    for(int i=0;i<n;i++){
        if(i>=poz && done<cate){
            done++;
            for(int j=i;j<n-1;j++){
                p[j]=p[j+1];
            }
            p=realloc(p,(n-1)*sizeof(char));
            //printf("%s\n",p);
            n--;
            i--;
        }
    }
    return p;
}

int main()
{
    FILE *fin = fopen("text.in","r");
    FILE *fout = fopen("text.out","w");
    fscanf(fin,"%d\n",&n);
    char *v=(char*) malloc(n*sizeof(char));
    char *p=(char*) malloc(4*sizeof(char));
    fgets(v,n,fin);
    fgets(p,100,fin);
    fgets(p,100,fin);
    int k=0;
    while(p[k]!='\0'){
        m++;
        k++;
    }

    v = sterg(v,2,3);
    fprintf(fout,"%s\n",v);

    v = inserez(v,p,2);

    fprintf(fout,"%s",v);

    free(v);
    fclose(fin);
    fclose(fout);
    return 0;
}
