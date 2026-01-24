#include <stdio.h>
#include <stdarg.h>
#include <string.h>

int sum(int count,int nr, ...) {
    va_list args;
    va_start(args,count);
    int rez=0;
    for (int i=0;i<count;i++) {
        if(va_arg(args, int)==nr)
            rez++;
    }
    va_end(args);
    return rez;
}

int main(){
    FILE* fin= fopen("text.in","r");
    FILE* fout= fopen("text.out","w");
    if(sum(4,1,1,1,1,1)==4)
        printf("DA");
    else
        printf("NU");
    return 0;
}
