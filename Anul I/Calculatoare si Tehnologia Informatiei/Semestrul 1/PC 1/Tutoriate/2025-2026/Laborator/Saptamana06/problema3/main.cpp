#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

char c1,c2;

char a[1005],b[1005];

int main()
{
    FILE *file1 = fopen("text.in","a+");
    //FILE *file2 = fopen("text.out","w+");
    fscanf(file1,"%c %c",&c1,&c2);

    //fgets(a,10,file1);
    fgets(a,1005,file1);

    int i=0;
    while(a[i]!='\n'){
        if(a[i]==' '){
            b[i]=' ';
            i++;
            continue;
        }
        if(a[i]>91){
            b[i]=a[i]-32;
        }
        if(a[i]<91){
            b[i]=a[i]+32;
        }
        i++;
    }
    fprintf(file1,"%s\n",b);
    return 0;
}
