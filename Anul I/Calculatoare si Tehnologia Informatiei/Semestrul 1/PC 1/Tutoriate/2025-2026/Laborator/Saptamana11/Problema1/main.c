#include <stdio.h>
#include <stdarg.h>
#include <string.h>

int msize=999999;

int min(int a,int b){
    if(a>=b)
        return b;
    return a;
}

void prefixcom(int count, char rez[], ...)
{
    va_list args;
    va_start(args, count);

    int h=0;
    for(int i=0;i<msize;i++)
    {
        va_list temp_args;
        va_copy(temp_args, args);

        char ver;
        int kon=0;
        char *parc=va_arg(temp_args, char*);
        ver=parc[i];
        for (int j=1;j<count;j++)
        {
            char *parc = va_arg(temp_args, char*);
            if (parc[i]==ver){
                kon++;
            }
        }
        if(kon==count-1){
            rez[h++]=ver;
        }
        else{
            break;
        }

        va_end(temp_args);
    }
    rez[h]='\0';

    va_end(args);
}


int main(){
    FILE* fin= fopen("text.in","r");
    FILE* fout= fopen("text.out","w");
    int n=4;
    char a[4][100];
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++){
        fscanf(fin,"%s",a[i]);
        msize = min(msize,strlen(a[i]));
    }
    char rez[1000];
    prefixcom(4,rez, a[0], a[1], a[2], a[3]);
    fprintf(fout,"%s",rez);
    return 0;
}
