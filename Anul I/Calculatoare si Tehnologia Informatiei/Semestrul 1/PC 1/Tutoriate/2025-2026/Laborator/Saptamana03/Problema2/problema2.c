#include <stdio.h>
#include <stdlib.h>

int v[1000];

int main(){
    int n,m;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&v[i]);
    }
    int x,y,xpoz,ypoz;
    scanf("%d %d",&x,&y);
    /// CAUTAREA BINARA pe x
    int st=0;
    int dr=n-1;
    while(st<=dr) {
        int mij=st+(dr-st)/2;
        if(v[mij]==x)
            xpoz=mij;
        if(v[mij]<x)
            st=mij+1;
        else
            dr=mij-1;
    }
    /// CAUTAREA BINARA pe y
    st=0;
    dr=n-1;
    while(st<=dr) {
        int mij=st+(dr-st)/2;
        if(v[mij]==y)
            ypoz=mij;
        if(v[mij]<y)
            st=mij+1;
        else
            dr=mij-1;
    }
    for(int i=xpoz;i<=ypoz;i++){
        printf("%d ",v[i]);
    }
    return 0;
}
