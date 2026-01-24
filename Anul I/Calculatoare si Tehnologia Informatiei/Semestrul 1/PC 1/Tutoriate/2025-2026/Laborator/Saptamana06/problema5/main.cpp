#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

char a[1005],b[1005];

int v[200];

int main()
{
    FILE *file1 = fopen("text.in","a+");
    FILE *file2 = fopen("text.out","w");

    fgets(a,1005,file1);

    int i=0,mare=0;
    while(a[i]!='\n'){
        char c;
        if(a[i]>96){
            c=a[i]-32;
        }
        v[c]++;
        if(v[c]>mare)
            mare=v[c];
        i++;
    }
    for(int i=0;i<200;i++){
        if(v[i]==mare){
            char c=char(i);
            fprintf(file2,"%c ",c);
        }
    }
    return 0;
}
