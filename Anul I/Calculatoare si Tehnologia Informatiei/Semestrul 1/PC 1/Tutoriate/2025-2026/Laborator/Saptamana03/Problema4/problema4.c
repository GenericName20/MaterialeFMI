#include <stdio.h>

int a[105][105], b[105][105];

int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%d",&a[i][j]);
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            b[j][i]=a[i][j];
        }
    }
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++){
            printf("%d ",b[i][j]);
        }
        printf("\n");
    }
}