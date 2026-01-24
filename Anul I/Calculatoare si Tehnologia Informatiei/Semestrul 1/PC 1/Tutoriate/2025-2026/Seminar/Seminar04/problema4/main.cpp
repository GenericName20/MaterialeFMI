#include <iostream>

using namespace std;

FILE *file1= fopen("numere.in","r");

void read(int *n,int v[]){
    for(int i=1;i<=*n;i++){
        fscanf(file1,"%d",&v[i]);
    }
    fclose(file1);
}

int maxsec(int i,int j,int v[]){
    int mare=0;
    for(int h=i;h<=j;h++){
        mare=max(v[h],mare);
    }
    return mare;
}

int i,j,n;
int v[1005];

int main()
{
    fscanf(file1,"%d",&n);
    read(&n,v);
    int mar=maxsec(1,n,v);
    int rez=0;
    for(int i=1;i<=n;i++){
        if(v[i]!=mar)
            rez=1;
    }
    printf("%d \n",mar);
    if(rez==0)printf("DA");
    else printf("NU");
    return 0;
}
