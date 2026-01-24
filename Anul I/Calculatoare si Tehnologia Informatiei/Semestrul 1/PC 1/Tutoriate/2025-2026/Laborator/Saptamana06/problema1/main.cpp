#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

char c;

char a[1005],b[1005];

int main()
{
    FILE *file1 = fopen("text.in","a+");
    FILE *file2 = fopen("text.out","w");
    fscanf(file1,"%c",&c);

    fgets(a,2,file1);
    fgets(a,1005,file1);

    int i=0,cnt=0;
    while(a[i]!='\n'){
        if(a[i]!=c){
            b[cnt]=a[i];
            fprintf(file2,"%c",a[i]);
            cnt++;
        }
        i++;
    }
    fprintf(file1,"%s\n",b);
    return 0;
}
