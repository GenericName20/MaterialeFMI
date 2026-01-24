#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    char w[1024],s[1024],t[1024];
    fscanf(fin,"%s",s);
    fscanf(fin,"%s",w);
    fscanf(fin,"%s",t);
    char gen[4096];
    char r[4096];
    int j=0;
    for(int i=0;i<strlen(w);i++){
        gen[j]=w[i];
        j++;
        if(strstr(gen,s)!=NULL){
            for(int h=0;h<=strlen(s);h++){
                gen[j]='\0';
                j--;
            }
            for(int h=0;h<=strlen(t);h++){
                j++;
                gen[j]=t[h];
            }
        }
    }
    fprintf(fout,"%s",gen);
    return 0;
}
