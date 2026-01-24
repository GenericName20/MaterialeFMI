#include <bits/stdc++.h>

using namespace std;

int n,k,cnt=0;

void reanj(int &cnt,int v[]){
    for(int i=1;i<=n;i++){
        if(v[i]==0){
            cnt++;
            for(int j=i+1;j<=n;j++){
                v[j-1]=v[j];
            }
        }
    }
}

int v[1005];

int main()
{
    FILE *file1 = fopen("text.in","r");
    FILE *file2 = fopen("date.out","w");
    fscanf(file1,"%d %d",&n,&k);
    for(int i=1;i<=n;i++){
        fscanf(file1,"%d",&v[i]);
    }
    reanj(cnt,v);
    for(int i=1;i<=n;i++){
        printf("%d ",v[i]);
    }
    printf("\n");
    if(cnt>=k){
        for(int i=0;i<k;i++){
            fprintf(file2,"0 ");
        }
    }
    fclose(file1);
    return 0;
}
